from django.urls import path

from articles import views

urlpatterns = [
    path('articles/forme/', views.get_fyp_articles),
    path('articles/random/', views.get_random_articles),
    path('articles/like/', views.LikeView.as_view()),
    path('articles/', views.get_dated_articles),
    path('categories/', views.CategoryView.as_view())
]
