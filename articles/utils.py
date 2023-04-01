import requests
import wikipediaapi
from datetime import datetime

from articles.models import Article, Category


def get_otd_articles():
    wiki_wiki = wikipediaapi.Wikipedia('en')
    day = datetime.now().day
    month = datetime.now().month
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/all/{month}/{day}").json()
    for i in response['selected']:
        page_py = wiki_wiki.page(i['pages'][0]['title'])
        article = Article.objects.create(title=page_py.title, abstract=page_py.summary[0:200], url=page_py.fullurl, day=day, month=month)
        for i in page_py.categories:
            cat = Category.objects.get_or_create(name=i)
            article.categories.add(cat)
        article.save()
