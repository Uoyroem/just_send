from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'chats', views.ChatViewSet, 'chat')
router.register(r'chats/(?P<chat_pk>[^/.]+)/messages',
                views.MessageViewSet, 'message')


app_name = 'chat'
urlpatterns = [
    path('', include(router.urls)),
]
