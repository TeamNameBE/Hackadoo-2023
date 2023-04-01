from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    interests = models.ManyToManyField("articles.Category")
    viewed_articles = models.ManyToManyField("articles.Article")
