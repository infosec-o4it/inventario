from django.contrib import admin
from .models import Metodologia, Dominio, Control, Registro, Grado, Madurez


# Register your models here.
class MetodologiaAdmin(admin.ModelAdmin):
    pass
    #list_display = ('nombre',)


class DominioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'metodologia')


class ControlAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dominio')


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('control', 'fecha', 'resultado')


class GradoAdmin(admin.ModelAdmin):
    pass
#list_display = ('nombre',)


class MadurezAdmin(admin.ModelAdmin):
    list_display = ('grado', 'fecha', 'registro')


admin.site.register(Metodologia, MetodologiaAdmin)
admin.site.register(Dominio, DominioAdmin)
admin.site.register(Control, ControlAdmin)
admin.site.register(Registro, RegistroAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Madurez, MadurezAdmin)

