# -*- coding: utf-8 -*-
from django.conf.urls import url

from informacion import views

urlpatterns = [
    # '',
    url(r'^buscar/', views.busca_activo, name='buscar'),
    url(r'^$', views.ingresa_activo, name='activo'),
]
