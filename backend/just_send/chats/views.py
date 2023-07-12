from rest_framework import viewsets
from . import serializers, models


class ChatViewSet(viewsets.ModelViewSet):
    lookup_url_kwarg = 'chat_pk'
    serializer_class = serializers.ChatSerializer
    queryset = models.Chat.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    lookup_url_kwarg = 'message_pk'

    serializer_class = serializers.MessageSerializer
    queryset = models.Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, chat=self.kwargs['chat_pk'])
