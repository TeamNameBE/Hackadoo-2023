from rest_framework import serializers

from articles.models import Article, Like


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'author', 'date')

    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('article', 'user')

    article = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user = serializers.CharField(max_length=100)
