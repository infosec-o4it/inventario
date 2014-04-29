from django.conf.urls import patterns, include, url
from model_report import report
report.autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^controles/', include('controles.urls')),
    url(r'^reportes/', include('model_report.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
