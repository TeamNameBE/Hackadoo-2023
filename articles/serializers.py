from rest_framework import serializers

from articles.models import Article, Like


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'abstract', 'url')

    title = serializers.CharField(max_length=100)
    abstract = serializers.CharField(max_length=200)
    url = serializers.URLField(max_length=200)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('article', 'user')

    article = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user = serializers.CharField(max_length=100)
