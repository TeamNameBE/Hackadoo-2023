import json
import os
import re
from urllib import parse, request

import requests
import wikipediaapi
from google.cloud import language_v1

from articles.models import Article, Category


list_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
               "December"]


def get_gif(search):
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
        "q": search,
        "api_key": os.environ.get("GIPHY_API_KEY"),
        "limit": "1"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())

    if len(data['data']) == 0:
        return None
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
    try:
        response = language_client.classify_text(request={"document": document})
        categories = response.categories

        result = {}

        for category in categories:
            # Turn the categories into a dictionary of the form:
            # {category.name: category.confidence}, so that they can
            # be treated as a sparse vector.
            result[category.name] = category.confidence

        if verbose:
            for category in categories:
                print("=" * 20)
                print("{:<16}: {}".format("category", category.name))
                print("{:<16}: {}".format("confidence", category.confidence))

        return [part for category in list(result.keys()) for part in category.split('/')[1:]]
    except Exception:
        return []


def get_otd_articles(day, month):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/all/{month}/{day}").json()
    print("processing events")
    for event in response['events']:
        max_page = -1
        for index, page in enumerate(event['pages']):
            if f"{list_months[month-1]}_{day}" == page['title']:
                continue
            if f"{day} {list_months[month-1]}" in page['extract']:
                max_page = index
            elif f"{list_months[month-1]} {day}" in page['extract']:
                max_page = index
        if max_page != -1:
            page_py = wiki_wiki.page(event['pages'][max_page]['title'])
            photo_url = None
            if max_page < len(event['pages']) and "originalimage" in event['pages'][max_page]:
                photo_url = event['pages'][max_page]['originalimage']['source']
            article, created = Article.objects.get_or_create(title=event['pages'][max_page]['titles']['normalized'],
                                                             abstract=page_py.summary,
                                                             url=page_py.fullurl,
                                                             day=day, month=month,
                                                             year=event['year'],
                                                             photo_url=photo_url,
                                                             gif_url=get_gif(page_py.title))
            if created:
                for category in classify(page_py.summary):
                    cat, _ = Category.objects.get_or_create(name=category)
                    article.subjects.add(cat)
                article.save()
    print("processing births")
    for event in response['births']:
        page_py = wiki_wiki.page(event['pages'][0]['title'])
        photo_url = None
        if "originalimage" in event['pages'][0]:
            photo_url = event['pages'][0]['originalimage']['source']
        article, created = Article.objects.get_or_create(title=page_py.title.replace("_", " "),
                                                         abstract=page_py.summary,
                                                         url=page_py.fullurl,
                                                         day=day, month=month,
                                                         year=event['year'],
                                                         photo_url=photo_url)
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
        photo_url = None
        if "originalimage" in event['pages'][0]:
            photo_url = event['pages'][0]['originalimage']['source']

        article, created = Article.objects.get_or_create(title=page_py.title.replace("_", " "),
                                                         abstract=page_py.summary,
                                                         url=page_py.fullurl,
                                                         day=day, month=month,
                                                         year=event['year'],
                                                         photo_url=photo_url)
        if created:
            cat, _ = Category.objects.get_or_create(name="Death")
            article.subjects.add(cat)
            # See if the summary is long enough to classify
            if len(page_py.summary.split()) > 20:
                for category in classify(page_py.summary):
                    cat, _ = Category.objects.get_or_create(name=category)
                    article.subjects.add(cat)
            article.save()
