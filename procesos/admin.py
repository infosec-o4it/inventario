from django.contrib import admin
from .models import procedimiento, area, persona, proceso, tipo,\
    entrada, salida, actividad

# Register your models here.


class procedimientoAdmin(admin.ModelAdmin):
    list_display = ('proceso', 'nombre', 'area')


class areaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


class personaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'area')


class procesoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'responsable', 'descripcion')


class tipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


class entradaAdmin(admin.ModelAdmin):
    list_display = ('proceso', 'tipo', 'descripcion')


class salidaAdmin(admin.ModelAdmin):
    list_display = ('proceso', 'tipo', 'descripcion')


class actividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'procedimiento')

admin.site.register(procedimiento, procedimientoAdmin)
admin.site.register(area, areaAdmin)
admin.site.register(persona, personaAdmin)
admin.site.register(proceso, procesoAdmin)
admin.site.register(tipo, tipoAdmin)
admin.site.register(entrada, entradaAdmin)
admin.site.register(salida, salidaAdmin)
admin.site.register(actividad, actividadAdmin)
