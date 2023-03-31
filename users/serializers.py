from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'interests', 'viewed_articles')        

    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    interests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    viewed_articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
