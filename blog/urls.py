# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog.views import about, article

__author__ = 'Petr Kashyapov'

urlpatterns = [
    url(r'^about/$', about, name='about'),
    url(r'^(?P<slug>[-\w]+)$', article, name='article'),
]