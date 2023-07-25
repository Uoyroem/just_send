from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from . import views


# TODO: Надо использовать библеотеку drf-nested-routers
default_router = DefaultRouter()
default_router.register(r'chats', views.ChatViewSet)

nested_default_router = NestedDefaultRouter(
    default_router, r'chats', lookup='chat')
nested_default_router.register(r'messages', views.MessageViewSet, 'message')

app_name = 'chats'
urlpatterns = [
    path('', include(default_router.urls)),
    path('', include(nested_default_router.urls))
]
