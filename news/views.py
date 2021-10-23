from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404

from django.conf import settings

import json


# Create your views here.

def index(request):
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>News Portal</title>
    </head>
    <body>
    <h1>Coming soon</h1>
        <ul>
          <li><a href="/news/" target="_blank">News</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(template);


def news(request):
    path = settings.BASE_DIR + '\\hypernews\\' + settings.NEWS_JSON_PATH
    with open(path, 'r', encoding='utf-8') as f:
        articels = json.loads(f.read())
        f.close()

    html = "\n".join(f"<li><a href='/news/{articel['link']}'>{articel['title']}</a></li>" for articel in articels)
    return HttpResponse(f"<ul>{html}</ul>")


def ArticelDetails(request, id):
    path = settings.BASE_DIR + '\\hypernews\\' + settings.NEWS_JSON_PATH
    with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as f:
        articels = json.loads(f.read())
        f.close()

    html = "<p>No Articel Found</p>"
    for articel in articels:
        if str(id) == str(articel['link']):
            html = "<h2>{title}</h2><p>{created}</p><p>{text}</p>".format(title=articel['title'],
                                                                          created=articel['created'],
                                                                          text=articel['text'])
    html = html + '<a href="/news/">Main Page</a>'
    return HttpResponse(html)
