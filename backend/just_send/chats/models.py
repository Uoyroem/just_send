from django.db import models
from django.contrib.auth import models as auth_models


class Chat(models.Model):
    users = models.ManyToManyField(auth_models.User, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(
        auth_models.User, on_delete=models.SET_DEFAULT, default=auth_models.AnonymousUser, related_name='messages')
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
