from rest_framework import serializers

from articles.models import Article, Like, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


class ArticleSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    media_url = serializers.SerializerMethodField()
    # subjects = CategorySerializer(read_only=True, many=True)

    def get_subject(self, obj):
        return obj.subjects.all()[0].name if obj.subjects.count() > 0 else "Misc"

    def get_media_url(self, obj):
        if "Sensitive Subjects" in obj.subjects.all().values_list('name', flat=True):
            return obj.photo_url or None
        else:
            return obj.gif_url or None
        
    class Meta:
        model = Article
        fields = ('id', 'title', 'abstract', 'url', 'media_url', 'subject', 'year')



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('article', 'user')

    article = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user = serializers.CharField(max_length=100)
