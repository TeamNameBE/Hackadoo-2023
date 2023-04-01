# Generated by Django 4.1.7 on 2023-04-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='gif_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='photo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]