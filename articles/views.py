from datetime import datetime

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView

from articles.models import Article, Category, Like
from articles.serializers import ArticleSerializer, LikeSerializer


@api_view(['GET'])
def get_fyp_articles(request):
    """
    **For You page**
    Here's the awesome algorithm that will get you the best articles
    """
    if not request.user.is_authenticated:
        return JsonResponse({"Error": "User not logged in"}, safe=False, status=401)
    user = request.user
    articles_list = Article.objects.filter(
        subjects__in=user.interests.all(),
        day=datetime.now().day,
        month=datetime.now().month
    ).order_by("?")[:10]
    # .exclude(
    #     id__in=user.viewed_articles.all().values_list('id', flat=True)
    # )

    data = []
    for article in articles_list:
        data.append(article)
        user.viewed_articles.add(article)

    serializer = ArticleSerializer(data, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_random_articles(request):
    """
    **Random page**
    Here's the awesome randomness that will get you the
    best random articles
    """

    user = request.user
    articles_list = Article.objects.filter(day=datetime.now().day, month=datetime.now().month).order_by("?")
    if user.is_authenticated:
        # articles_list = articles_list.exclude(
        #     id__in=user.viewed_articles.all().values_list('id', flat=True)
        # )
        pass
    articles_list = articles_list.exclude(
        subjects__in=Category.objects.filter(name__in=["Death", "Birth"])
    )[:10]

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
