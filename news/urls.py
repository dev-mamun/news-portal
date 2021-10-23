# Created by Md.Abdullah Al Mamun
# Project: HyperNews Portal
# File: urls.py
# Email: dev.mamun@gmail.com
# Date: 10/8/2021
# Time: 3:28 PM
# Year: 2021

"""hypernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index),
    path('news/', views.news),
    re_path(r"news/(?P<id>\d+)/$", views.ArticelDetails)
]
