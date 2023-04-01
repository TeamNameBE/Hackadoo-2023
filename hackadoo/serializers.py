from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class EmailJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {"username": "", "password": attrs.get("password")}

        # iexact for case insensitive
        if user_obj := User.objects.filter(email__iexact=attrs.get("username")).first():
            credentials["username"] = user_obj.username

        return super().validate(credentials)
