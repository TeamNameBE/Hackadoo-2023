import requests
import wikipediaapi
from datetime import datetime

from articles.models import Article, Category


def get_otd_articles(day, month):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/all/{month}/{day}").json()
    for j in response['selected']:
        max_len = 0
        max_page = 0
        for index, i in enumerate(j['pages']):
            if len(i['extract']) > max_len:
                max_len = len(i['extract'])
                max_page = index
        page_py = wiki_wiki.page(j['pages'][max_page]['title'])
        article = Article.objects.create(title=page_py.title, abstract=page_py.summary[0:200], url=page_py.fullurl, day=day, month=month, year=j['year'])
        for i in page_py.categories:
            cat = Category.objects.get_or_create(name=i)
            article.categories.add(cat)
        article.save()
