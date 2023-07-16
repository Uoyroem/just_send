from django.urls import path, include
from rest_framework import routers
from . import views

# TODO: Надо использовать библеотеку drf-nested-routers
router = routers.DefaultRouter()
router.register(r'chats', views.ChatViewSet)
router.register(r'chats/(?P<chat_pk>[^/.]+)/messages',
                views.MessageViewSet)


app_name = 'chat'
urlpatterns = [
    path('', include(router.urls)),
]
