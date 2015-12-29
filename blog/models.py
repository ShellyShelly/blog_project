# -*- coding: utf-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    summary = RichTextUploadingField(blank=True, default='')
    content = RichTextUploadingField(blank=True, default='')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-time']

