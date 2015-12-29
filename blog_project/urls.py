# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import home
from blog import urls as blog_urls
from django.conf.urls.static import static
from blog_project import settings

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^blog/', include(blog_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)