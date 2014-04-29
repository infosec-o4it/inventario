from django.contrib import admin
from .models import tipo, activo, area, usuario, niveles_acceso, datacenter
from django.http import HttpResponse

import csv


def prep_field(obj, field):
    """ Returns the field as a unicode string. If the field is a callable, it
    attempts to call it first, without arguments.
    """
    if '__' in field:
        bits = field.split('__')
        field = bits.pop()

        for bit in bits:
            obj = getattr(obj, bit, None)

            if obj is None:
                return ""

    attr = getattr(obj, field)
    output = attr() if callable(attr) else attr
    return unicode(output).encode('utf-8') if output else ""


def export_csv_action(description="Export as CSV",
                      fields=None, exclude=None, header=True):
    """ This function returns an export csv action. """
    def export_as_csv(modeladmin, request, queryset):
        """ Generic csv export admin action.
        Based on http://djangosnippets.org/snippets/2712/
        """
        opts = modeladmin.model._meta
        field_names = [field.name for field in opts.fields]
        labels = []

        if exclude:
            field_names = [f for f in field_names if f not in exclude]

        elif fields:
            field_names = [field for field, _ in fields]
            labels = [label for _, label in fields]

        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % (
                unicode(opts).replace('.', '_')
            )

        writer = csv.writer(response)

        if header:
            writer.writerow(labels if labels else field_names)

        for obj in queryset:
            writer.writerow([prep_field(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv

# Register your models here.


class activoAdmin(admin.ModelAdmin):
    list_display = ('activo', 'tipo',
        'propietario', 'responsable',
        'confidencialidad', 'integridad', 'disponibilidad')
    search_fields = ('activo', 'propietario__cargo')
    list_filter = ('area', 'ubicacion', 'propietario', 'responsable', 'tipo')
    actions = [
        export_csv_action("Export Sepecial Report",
            fields=[
                ('pk', 'id'),
                ('activo', 'activo'),
                ('descripcion', 'descripcion'),
                ('tipo', 'label3'),
                ('ubicacion', 'ubicacion'),
                ('area', 'area'),
                ('propietario', 'propietario'),
                ('responsable', 'responsable'),
                ('usuario', 'usuario'),
                ('funcion', 'funcion'),
                ('datos_personales', 'datos personales'),
                ('propia', 'propia'),
                ('terceros', 'terceros'),
                ('clientes', 'clientes'),
                ('confidencialidad', 'confidencialidad'),
                ('integridad', 'integridad'),
                ('disponibilidad', 'disponibilidad'),
            ],
            header=True,
        ),
    ]


class areaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


class usuarioAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'area')


class niveles_accesoAdmin(admin.ModelAdmin):
    list_display = ('activo', 'usuario')
    search_fields = ('activo', 'usuario')

admin.site.register(area, areaAdmin)
admin.site.register(usuario, usuarioAdmin)
admin.site.register(niveles_acceso, niveles_accesoAdmin)
admin.site.register(tipo)
admin.site.register(datacenter)
admin.site.register(activo, activoAdmin)
