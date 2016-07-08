"""tagz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^tagz/$', views.home, name='tagz'),
    url(r'^tagz/chunks/$', views.get_chunks, name='chunks'),
    url(r'^tagz/tag/new/$', views.new_tag, name='new-tag'),
    url(r'^tagz/tag/delete/$', views.delete_tag, name='delete-tag'),
    url(r'^tagz/chunk/new/$', views.new_chunk, name='new-chunk'),
    url(r'^tagz/chunk/delete/$', views.delete_chunk, name='delete-chunk'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
]
