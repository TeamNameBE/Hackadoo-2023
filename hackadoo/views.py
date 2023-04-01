from django.conf import settings
from django.shortcuts import render


def home(request):

    context = {
        'page_title': "The Time Traveler's Gazette",
    }

    if settings.DEBUG:
        return render(request, 'index_debug.html', context=context)
    return render(request, 'index.html', context=context)
