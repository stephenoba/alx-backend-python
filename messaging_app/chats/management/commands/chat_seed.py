from django.utils import timezone
import inspect

# Monkeypatch make_aware to accept is_dst (temporary workaround for Django 5)
_orig_make_aware = timezone.make_aware
if 'is_dst' not in inspect.signature(_orig_make_aware).parameters:
    def _make_aware(dt, tz=None, is_dst=None):
        return _orig_make_aware(dt, tz)
    timezone.make_aware = _make_aware

from chats.models import User, Message, Conversation
from django.core.management.base import BaseCommand
from django_seed import Seed

class Command(BaseCommand):
    help = 'Seed the database with initial data for testing and development'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        # Seed Users first
        seeder.add_entity(User, 10, {
            'first_name': lambda x: seeder.faker.first_name(),
            'last_name': lambda x: seeder.faker.last_name(),
            'email': lambda x: seeder.faker.unique.email(),
            'password_hash': lambda x: seeder.faker.password(),
            'phone_number': lambda x: seeder.faker.phone_number(),
            'role': lambda x: seeder.faker.random_element(elements=['guest', 'host', 'admin']),
        })

        # Seed Conversations
        seeder.add_entity(Conversation, 5, {
           'participants_id': lambda x: User.objects.order_by('?').first(),
        })

        inserted_pks_phase1 = seeder.execute()
        def _pks(mapping, model):
            return mapping.get(model) or mapping.get(model.__name__) or []

        # Now seed Messages and ensure each message has a conversation and sender
        seeder2 = Seed.seeder()
        seeder2.add_entity(Message, 20, {
            'sender_id': lambda x: User.objects.order_by('?').first(),
            'message_body': lambda x: seeder2.faker.text(max_nb_chars=200),
        })

        inserted_pks_phase2 = seeder2.execute()

        total_created = sum(len(v) for v in inserted_pks_phase1.values()) + sum(len(v) for v in inserted_pks_phase2.values())
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded database with {total_created} records.'))
