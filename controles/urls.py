# -*- coding: utf-8 -*-
from django.conf.urls import url

from controles import views

urlpatterns = [
    # '',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<control_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<control_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<control_id>\d+)/vote/$', views.vote, name='vote'),
]
