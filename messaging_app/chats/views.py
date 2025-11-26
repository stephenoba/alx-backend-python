from django.shortcuts import render

from rest_framework import viewsets

from .models import User, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(participants_id=user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer