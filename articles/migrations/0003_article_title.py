# Generated by Django 4.1.7 on 2023-04-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='Insert Title', max_length=200),
        ),
    ]