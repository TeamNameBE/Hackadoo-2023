from rest_framework import serializers

from users.models import User
from articles.serializers import ArticleSerializer, CategorySerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'interests', 'viewed_articles')

    interests = CategorySerializer(many=True, read_only=True)
    viewed_articles = ArticleSerializer(many=True, read_only=True)
