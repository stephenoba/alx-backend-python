from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a participant in the conversation
        return request.user in obj.participants_id.all() and request.user.is_authenticated
    
    def has_permission(self, request, view):
        # Allow access only to authenticated users
        return request.user and request.user.is_authenticated