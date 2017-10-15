from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'second', views.second, name='second'),
    url(r'third/(?P<id>[0-9]+)/$', views.third, name='third')
]
