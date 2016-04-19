from django.conf.urls import include, url
# from model_report import report
# report.autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'inventario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^informacion/', include('informacion.urls')),
    url(r'^seguimientos/', include('seguimiento.urls')),
    url(r'^controless/', include('controles.urls')),
    # url(r'^reportes/', include('model_report.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
