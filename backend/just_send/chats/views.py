from rest_framework import viewsets
from . import serializers, models


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChatSerializer
    queryset = models.Chat.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        return models.Message.objects.filter(chat=self.kwargs['chat_pk'])

    def perform_create(self, serializer):
        serializer.save(
            sender=self.request.user if self.request.user.is_authenticated else None, chat_id=self.kwargs['chat_pk'])
