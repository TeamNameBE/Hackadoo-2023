import json
import os
import re
from urllib import parse, request

import requests
import wikipediaapi
from google.cloud import language_v1

from articles.models import Article, Category


def get_gif(search):
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
        "q": search,
        "api_key": os.environ.get("GIPHY_API_KEY"),
        "limit": "1"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())

    return data['data'][0]['images']['original']['url']


def classify(text, verbose=False):
    """Classify the input text into categories."""

    text = re.sub(r'[^\x00-\x7f]', r'', text)

    language_client = language_v1.LanguageServiceClient(
        client_options={
            "api_key": os.environ.get("GOOGLE_API_KEY")
        }
    )

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(request={"document": document})
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print("=" * 20)
            print("{:<16}: {}".format("category", category.name))

            print("{:<16}: {}".format("confidence", category.confidence))

    return [part for category in list(result.keys()) for part in category.split('/')[1:]]


def get_otd_articles(day, month):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/all/{month}/{day}").json()
    print("processing events")
    for event in response['events']:
        max_len = 0
        max_page = 0
        for index, page in enumerate(event['pages']):
            if len(page['extract']) > max_len:
                max_len = len(page['extract'])
                max_page = index
        page_py = wiki_wiki.page(event['pages'][max_page]['title'])
        article, created = Article.objects.get_or_create(title=page_py.title,
                                                   abstract=page_py.summary,
                                                   url=page_py.fullurl,
                                                   day=day, month=month,
                                                   year=event['year'],
                                                   photo_url=event['pages'][max_page]['originalimage']['source'],
                                                   gif_url=get_gif(page_py.title))
        if created:
            for category in classify(page_py.summary):
                cat, _ = Category.objects.get_or_create(name=category)
                article.subjects.add(cat)
            article.save()
    print("processing births")
    for event in response['births']:
        page_py = wiki_wiki.page(event['pages'][0]['title'])
        article, created = Article.objects.get_or_create(title=page_py.title,
                                                   abstract=page_py.summary,
                                                   url=page_py.fullurl,
                                                   day=day, month=month,
                                                   year=event['year'],
                                                   photo_url=event['pages'][max_page]['originalimage']['source'])
        if created:
            cat, _ = Category.objects.get_or_create(name="Birth")
            article.subjects.add(cat)
            if len(page_py.summary.split()) > 20:
                for category in classify(page_py.summary):
                    cat, _ = Category.objects.get_or_create(name=category)
                    article.subjects.add(cat)
            article.save()
    print("processing deaths")
    for event in response['deaths']:
        page_py = wiki_wiki.page(event['pages'][0]['title'])
        article, created = Article.objects.get_or_create(title=page_py.title,
                                                   abstract=page_py.summary,
                                                   url=page_py.fullurl,
                                                   day=day, month=month,
                                                   year=event['year'],
                                                   photo_url=event['pages'][max_page]['originalimage']['source'])
        if created:
            cat, _ = Category.objects.get_or_create(name="Death")
            article.subjects.add(cat)
            # See if the summary is long enough to classify
            if len(page_py.summary.split()) > 20:
                for category in classify(page_py.summary):
                    cat, _ = Category.objects.get_or_create(name=category)
                    article.subjects.add(cat)
            article.save()
