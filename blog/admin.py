# -*- coding: utf-8 -*-
from django.contrib import admin

from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'time')

admin.site.register(Article, ArticleAdmin)
