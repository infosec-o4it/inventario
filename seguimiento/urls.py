# -*- coding: utf-8 -*-
from django.conf.urls import url

from seguimiento import views

urlpatterns = [
    # '',
    url(r'^$', views.index, name='inxdex'),
]
