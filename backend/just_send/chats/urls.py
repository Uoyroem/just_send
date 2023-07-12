from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'chats', views.ChatViewSet, 'chats')
router.register(r'chats/<int:pk>', views.MessageViewSet, 'messages')


app_name = 'chat'
urlpatterns = [
    path('', include(router.urls)),
]
