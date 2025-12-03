from django.contrib import admin
from .models import User, Message, Conversation


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('role', 'created_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'sender_id', 'message_body', 'sent_at')
    search_fields = ('sender_id__email', 'message_body')
    list_filter = ('sent_at',)

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_id', 'created_at')
    search_fields = ('participants_id__email',)
    list_filter = ('created_at',)


