# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from blog.models import Article


def home(request):
    return TemplateResponse(request, 'index.html', {'articles': Article.objects.all()[0:10]})

def about(request):
    return TemplateResponse(request, 'about.html', {'articles': Article.objects.all()[0:10]})

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return TemplateResponse(request, 'article.html', {'article': article, 'articles': Article.objects.all()[0:10]})