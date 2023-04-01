from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    interests = models.ManyToManyField("articles.Category")
    viewed_articles = models.ManyToManyField("articles.Article")
