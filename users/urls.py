from django.urls import path

from users import views

urlpatterns = [
    path('', views.UpdateUser.as_view()),
]
