# Generated by Django 4.1.7 on 2023-04-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0005_article_gif_url_article_photo_url"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="viewed_articles",
            field=models.ManyToManyField(blank=True, to="articles.article"),
        ),
    ]
