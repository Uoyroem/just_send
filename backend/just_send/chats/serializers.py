
from rest_framework.serializers import ModelSerializer
from . import models


class ChatSerializer(ModelSerializer):
    class Meta:
        model = models.Chat
        fields = '__all__'
        

class MessageSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'
