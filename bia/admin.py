# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ProcesoBia, CapitalTiempo, AplicacionesTiempo
from .models import PersonasTiempo, CanalesActividad, CanalesTiempo
from .models import DocumentosActividad, DocumentosTiempo, EquiposTIActividad
from .models import EquiposTiTiempo, EquiposNoTIActividad, EquiposNoTiTiempo
from .models import InstalacionesActividad, InstalacionesTiempo, PapelActividad
from .models import PapelTiempo, ServiciosExternosActividad, ServiciosTiempo
from .models import RyLImpacto, ServicioClienteImpacto, ImagenImpacto
from .models import IngresosImpacto, GastosImpacto, AplicacionesImpacto
from .models import DocumentoImpacto, PapelImpacto, Actividad
# Register your models here.
admin.site.register(ProcesoBia, ProcesoBia.Admin)
admin.site.register(CapitalTiempo, CapitalTiempo.Admin)
admin.site.register(AplicacionesTiempo, AplicacionesTiempo.Admin)
admin.site.register(PersonasTiempo, PersonasTiempo.Admin)
admin.site.register(CanalesActividad, CanalesActividad.Admin)
admin.site.register(CanalesTiempo, CanalesTiempo.Admin)
admin.site.register(DocumentosActividad, DocumentosActividad.Admin)
admin.site.register(DocumentosTiempo, DocumentosTiempo.Admin)
admin.site.register(EquiposTIActividad, EquiposTIActividad.Admin)
admin.site.register(EquiposTiTiempo, EquiposTiTiempo.Admin)
admin.site.register(EquiposNoTIActividad, EquiposNoTIActividad.Admin)
admin.site.register(EquiposNoTiTiempo, EquiposNoTiTiempo.Admin)
admin.site.register(InstalacionesActividad, InstalacionesActividad.Admin)
admin.site.register(InstalacionesTiempo, InstalacionesTiempo.Admin)
admin.site.register(PapelActividad, PapelActividad.Admin)
admin.site.register(PapelTiempo, PapelTiempo.Admin)
admin.site.register(ServiciosExternosActividad,
                    ServiciosExternosActividad.Admin)
admin.site.register(ServiciosTiempo, ServiciosTiempo.Admin)
admin.site.register(RyLImpacto, RyLImpacto.Admin)
admin.site.register(ServicioClienteImpacto, ServicioClienteImpacto.Admin)
admin.site.register(ImagenImpacto, ImagenImpacto.Admin)
admin.site.register(IngresosImpacto, IngresosImpacto.Admin)
admin.site.register(GastosImpacto, GastosImpacto.Admin)
admin.site.register(AplicacionesImpacto, AplicacionesImpacto.Admin)
admin.site.register(DocumentoImpacto, DocumentoImpacto.Admin)
admin.site.register(PapelImpacto, PapelImpacto.Admin)
admin.site.register(Actividad, Actividad.Admin)
