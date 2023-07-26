from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from . import serializers
from django.contrib.auth.models import User

class UserReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = serializers.IdUsernameSerializer
    queryset = User.objects.all()

    @action(methods=['POST'], detail=False, serializer_class=serializers.UsernamePasswordSerializer)
    def register(self, request):
        user = User.objects.create_user(**request.data)
        user.save()
