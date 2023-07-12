from rest_framework import viewsets
from . import serializers, models


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChatSerializer
    queryset = models.Chat.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer
    queryset = models.Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(chat=self.kwargs['chat_id'])
