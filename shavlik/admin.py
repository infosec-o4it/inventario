from django.contrib import admin
from .models import Cliente, OS, Dominio, Datacenter, Rol, Servidores


class clienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente',)


class osAdmin(admin.ModelAdmin):
    list_display = ('nombre_os',)


class dominioAdmin(admin.ModelAdmin):
    list_display = ('nombre_dominio',)


class rolAdmin(admin.ModelAdmin):
    list_display = ('nombre_rol',)


class datacenterAdmin(admin.ModelAdmin):
    list_display = ('nombre_datacenter',)


class servidorAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip', 'datacenter', 'sistema_operativo',
                    'cliente', 'dominio', 'rol', 'fecha_programada', 'shavlik')
    search_fields = ('hostname', 'ip', 'dominio__nombre_dominio')
    list_filter = ('datacenter', 'dominio', 'cliente', 'sistema_operativo',
                   'rol', 'fecha_programada', 'shavlik')

admin.site.register(Cliente, clienteAdmin)
admin.site.register(OS, osAdmin)
admin.site.register(Rol, rolAdmin)
admin.site.register(Datacenter, datacenterAdmin)
admin.site.register(Servidores, servidorAdmin)
admin.site.register(Dominio, dominioAdmin)
