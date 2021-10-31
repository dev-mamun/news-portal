import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404

from django.conf import settings

import json
import copy


def _get_news(file_news):
    with open(file_news, "r") as f:
        news = json.load(f)
    return news


def _get_dates(news, string=""):
    items = copy.deepcopy(news)
    items = sorted(items, key=lambda item: item["created"], reverse=True)
    for item in items:
        item["created"] = item["created"][:10]
    dates = dict()
    date = ""
    for item in items:
        if string and string not in item["title"]:
            continue
        if item["created"] == date:
            dates[date].append(item)
        else:
            date = item["created"]
            dates[date] = [item]
    return dates


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


class News(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get("q")
        news = _get_news(settings.NEWS_JSON_PATH)
        dates = _get_dates(news, search)
        context = {'dates': dates}
        return render(request, 'news.html', context=context)


class NewsDetails(View):
    def get(self, request, link, *args, **kwargs):
        news_data = _get_news(settings.NEWS_JSON_PATH)
        for news in news_data:
            if link == news['link']:
                return render(request, 'news2.html', context=news)


def all_news(request):
    return render(request, 'news.html', {'news': _get_news(settings.NEWS_JSON_PATH)})

def news(request):
    with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as f:
        articels = json.loads(f.read())
        f.close()

    articels = sorted(articels, key=lambda k: k['created'], reverse=True)

    html = "<h2>Hyper news</h2>"
    created_date = []
    for articel in articels:
        created = datetime.datetime.strptime(articel['created'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        title = articel['title']
        link = str(articel['link'])
        if created in created_date:
            h4 = ""
        else:
            created_date.append(created)
            h4 = "<h4>" + created + "</h4>"
        html += h4 + "<ul><li><a href='/news/" + link + "' target='_blank'>" + title + "</a></li></ul>"
    html += '<a href="/news/create/">/news/create/</a>'

    return HttpResponse(html)

def ArticelDetails(request, id):
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
