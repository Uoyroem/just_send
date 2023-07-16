
from rest_framework.serializers import ModelSerializer
from . import models


class ChatSerializer(ModelSerializer):
    class Meta:
        model = models.Chat
        fields = ['id', 'title', 'thumbnail', 'created_at']


class MessageSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['id', 'sender', 'chat',
                  'message', 'created_at', 'updated_at']
        read_only_fields = ['sender', 'chat']
