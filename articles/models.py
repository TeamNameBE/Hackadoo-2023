from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200, default="Insert Title")
    abstract = models.TextField(default="Insert content")
    subjects = models.ManyToManyField(Category)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    photo_url = models.URLField(blank=True, null=True)
    gif_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
