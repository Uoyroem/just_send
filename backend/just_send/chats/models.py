from django.db import models
from django.contrib.auth import models as auth_models


class Chat(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='chats/thumbnails')
    users = models.ManyToManyField(
        auth_models.User, related_name='chats', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(
        auth_models.User, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='messages', blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
