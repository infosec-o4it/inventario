from django.contrib import admin
from .models import RegistroElemento, RecuperacionElemento, UbicacionElemento
from .models import RetencionElemento, DisposicionElemento
# Register your models here.


class RegistrosAdmin(admin.ModelAdmin):
    list_filter = ('proceso',)
    list_display = ('proceso', 'codigo', 'nombre', 'recuperacion', 'ubicacion',
                    'retencion', 'disposicion',)

admin.site.register(RegistroElemento, RegistrosAdmin)


class RecuperacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(RecuperacionElemento, RecuperacionAdmin)


class UbicacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(UbicacionElemento, UbicacionAdmin)


class RetencionAdmin(admin.ModelAdmin):
    pass

admin.site.register(RetencionElemento, RetencionAdmin)


class DisposicionAdmin(admin.ModelAdmin):
    pass

admin.site.register(DisposicionElemento, DisposicionAdmin)
