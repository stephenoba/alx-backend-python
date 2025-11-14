from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    GUEST = 'guest', 'Guest'
    HOST = 'host', 'Host'
    ADMIN = 'admin', 'Admin'


class User(AbstractUser):
    """Custom user model extending AbstractUser."""
    user_id = models.UUIDField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password_hash = models.CharField(max_length=128, null=False, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    role = models.CharField(max_length=20, null=False, blank=False, choices=Role.choices, default=Role.GUEST)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} ({self.email})"
    

class Message(models.Model):
    """Model representing a chat message."""
    message_id = models.UUIDField(primary_key=True, editable=False)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender_id.email} at {self.sent_at}"
    

class Conversation(models.Model):
    """Model representing a conversation between users."""
    conversation_id = models.UUIDField(primary_key=True, editable=False)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id} with participant {self.participants_id.email}"