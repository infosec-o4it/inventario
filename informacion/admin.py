from django.contrib import admin
from models import tipo, activo, area, usuario, niveles_acceso

# Register your models here.
class activoAdmin(admin.ModelAdmin):
    list_display = ('activo', 'tipo', 'propietario','responsable')
    search_fields = ('activo', 'propietario')

class areaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    
class usuarioAdmin(admin.ModelAdmin):
    list_display = ('cargo','area')

class niveles_accesoAdmin(admin.ModelAdmin):
    list_display = ('activo', 'usuario')
    search_fields = ('activo', 'usuario')
    
admin.site.register(area,areaAdmin)
admin.site.register(usuario,usuarioAdmin)
admin.site.register(niveles_acceso,niveles_accesoAdmin)
admin.site.register(tipo)
admin.site.register(activo,activoAdmin)