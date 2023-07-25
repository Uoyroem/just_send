from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrParticipantReadonly(BasePermission):
    def has_permission(self, request, view):
        chat = view.get_object()
        return request.user in chat.participants and request.method in SAFE_METHODS or request.user == chat.owner

    
