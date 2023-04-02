from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UpdateUser(RetrieveUpdateAPIView):
    lookup_field = 'username'
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        username = self.request.user.username
        return get_object_or_404(User, username=username)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
