from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView

from django.http import JsonResponse

from articles.serializers import ArticleSerializer, LikeSerializer
from articles.models import Article, Like


@api_view(['GET'])
def get_fyp_articles(request):
    user = request.user
    articles_list = Article.objects.filter(subjects__in=user.interests.all(), day=datetime.now().day,
                                           month=datetime.now().month).exclude(user.viewed_articles.all()).order_by("?")[:10]
    data = []
    for article in articles_list:
        data.append(article)
        user.viewed_articles.add(article)

    serializer = ArticleSerializer(data, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_random_articles(request):
    user = request.user
    articles_list = Article.objects.all().order_by("?")
    if user.is_authenticated:
        # articles_list = articles_list.exclude(
        #     id__in=user.viewed_articles.all().values_list('id', flat=True)
        # )
        pass
    articles_list = articles_list[:10]
    data = []
    for article in articles_list:
        data.append(article)
        if user.is_authenticated:
            user.viewed_articles.add(article)

    serializer = ArticleSerializer(data, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_dated_articles(request):
    user = request.user
    if user.is_authenticated:
        articles_list = Article.objects.filter(year=request.query_params.get('year')).exclude(user.viewed_articles.all()).order_by("?")[:10]
    else:
        articles_list = Article.objects.filter(year=request.query_params.get('year')).order_by("?")[:10]
    data = []
    for article in articles_list:
        data.append(article)
        user.viewed_articles.add(article)

    serializer = ArticleSerializer(data, many=True)

    return JsonResponse(serializer.data, safe=False)


class LikeView(CreateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def create(self, request):
        user = request.user
        article = Article.objects.get(id=request.data.get('article_id'))
        Like.objects.create(user=user, article=article)
        return JsonResponse({'status': 'success'})
