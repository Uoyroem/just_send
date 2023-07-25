from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class IdUsernameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class UsernamePasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']