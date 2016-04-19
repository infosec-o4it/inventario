from django.contrib import admin
from models import seccion, control, numeral, punto, hallazgo
# Register your models here.

admin.site.register(seccion)
admin.site.register(control)
admin.site.register(numeral)


class puntoAdmin(admin.ModelAdmin):
    list_display = ('numeral', 'id', 'pregunta')
    search_fields = ('numeral', 'pregunta')

admin.site.register(punto, puntoAdmin)


class hallazgoAdmin(admin.ModelAdmin):
    list_display = ('punto', 'resumen', 'usuario', 'nota')
    search_fields = ("punto", "resumen", "usuario__cargo", "fecha")
    list_filter = ("punto__numeral__control", "resumen", "usuario__cargo",
                   "fecha", "nota",)
    raw_id_fields = ("punto", "usuario")

admin.site.register(hallazgo, hallazgoAdmin)
