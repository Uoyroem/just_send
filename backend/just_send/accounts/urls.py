from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


default_router = routers.DefaultRouter()
default_router.register('users', views.UserReadOnlyViewSet)

app_name = 'accounts'
urlpatterns = [
    path('', include(default_router.urls)),
    path('users/login', TokenObtainPairView.as_view(), name='login'),
    path('users/refresh', TokenRefreshView.as_view(), name='refresh')
]