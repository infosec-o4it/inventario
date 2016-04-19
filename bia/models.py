# -*- coding: utf-8 -*-
from django.db import models
import datetime
from informacion.models import usuario, activo
from informacion.models import usuario
from django.contrib import admin
# Create your models here.

ImpactoCuantitativo = (
    (0, 'Ninguno'),
    (1, '< 1000'),
    (2, '>= 1000 < 5000'),
    (3, '>= 5000 < 10000'),
    (4, '>= 10000 < 25000'),
    (5, '>= 25000 < 50000'),
    (6, '>= 50000 < 100000'),
    (7, '>= 100000 < 150000'),
    (8, '>= 150000 < 250000'),
    (9, '>= 250000 < 500000'),
    (10, '>= 500000'),
)


class ProcesoBia(models.Model):
    """(ProcesoBia description)"""
    """ Modelo para almacenar los proceso a evaluar para BIA"""
    Nombre_de_Proceso = models.CharField(max_length=100, unique=True)
    Lider_del_Proceso = models.ForeignKey(usuario)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre_de_Proceso', 'Lider_del_Proceso')
        search_fields = ('Nombre_de_Proceso', 'Lider_del_Proceso')

    def __unicode__(self):
        return u"Proceso %s" % (self.Nombre_de_Proceso)


class CapitalTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Capital = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCuantitativo)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Capital', 'Descripcion')
        search_fields = ('Capital', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.Aplicacion, self.Descripcion)


class AplicacionesTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Aplicacion = models.ForeignKey(activo)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Aplicacion', 'Descripcion')
        search_fields = ('Aplicacion', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (str(self.Aplicacion).encode('utf8'),
                           self.Descripcion)


class PersonasTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Cargo = models.ForeignKey(usuario)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Cargo', 'Descripcion')
        search_fields = ('Cargo', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.Cargo, self.Descripcion)


class CanalesActividad(models.Model):
    """(CanalesActividad description)"""
    """ modelo para almacenar los tipos de canales de red o isp's que pueda
    requerir una Actividad segun el BIA """
    Nombre = models.CharField(max_length=100)
    Ancho_de_Banda = models.CharField(max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Ancho_de_Banda',)
        search_fields = ('Nombre', 'Ancho_de_Banda',)

    def __unicode__(self):
        return u"Canal %s - %s" % (self.Nombre, self.Ancho_de_Banda)


class CanalesTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Canal = models.ForeignKey(CanalesActividad)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Canal', 'Descripcion')
        search_fields = ('Canal', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.Canal, self.Descripcion)


class DocumentosActividad(models.Model):
    """(DocumentosActividad description)"""
    """ Modelo basico para almacenar los documentos o formatos que sean
    necesarios para atender o responder a una emergencia """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(blank=True, max_length=100)
    Documento_copia = models.FileField(blank=True, null=True,
                                       upload_to='./upload')

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Descripcion')
        search_fields = ('Nombre', 'Descripcion')

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class DocumentosTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Documento = models.ForeignKey(DocumentosActividad)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Documento', 'Descripcion')
        search_fields = ('Documento', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.Documento, self.Descripcion)


class EquiposTIActividad(models.Model):
    """(EquiposTIActividad description)"""
    """ modelo basico para almacenar datos de equipos de TI necesarios para
    alguna emergencia """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Descripcion')
        search_fields = ('Nombre', 'Descripcion')

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class EquiposTiTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    EquipoTi = models.ForeignKey(EquiposTIActividad)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('EquipoTi', 'Descripcion')
        search_fields = ('EquipoTi', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.EquipoTi, self.Descripcion)


class EquiposNoTIActividad(models.Model):
    """(EquiposNoTIActividad description)"""
    """ modelo basico para almacenar datos de los equipos no TI necesarios para
    atender alguna emergencia """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Descripcion')
        search_fields = ('Nombre', 'Descripcion')

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class EquiposNoTiTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    EquipoNoTi = models.ForeignKey(EquiposNoTIActividad)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('EquipoNoTi', 'Descripcion')
        search_fields = ('EquipoNoTi', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.EquipoNoTi, self.Descripcion)


class InstalacionesActividad(models.Model):
    """(InstalacionesActividad description)"""
    """ Modelo basico para almacenar las instalaciones o infraestructuras para
    atender o responder una emergencia """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Descripcion')
        search_fields = ('Nombre', 'Descripcion')

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class InstalacionesTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Instalaciones = models.ForeignKey(InstalacionesActividad)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Instalaciones', 'Descripcion')
        search_fields = ('Instalaciones', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.Instalaciones, self.Descripcion)


class PapelActividad(models.Model):
    """(PapelActividad description)"""
    """modelo basico para almacenar datos de documentos en papel necesarios para
    atender una emergencia """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(blank=True, max_length=100)
    Version_digital = models.FileField(blank=True, null=True,
                                       upload_to='./upload')

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Descripcion')
        search_fields = ('Nombre', 'Descripcion')

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class PapelTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Papel = models.ForeignKey(PapelActividad)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Papel', 'Descripcion')
        search_fields = ('Papel', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.Papel, self.Descripcion)


class ServiciosExternosActividad(models.Model):
    """(ServiciosExternosActividad description)"""
    """ modelo basico para almacenar informacion de proveedores o servicios
    externos necesarios para atender una emergencia """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Descripcion')
        search_fields = ('Nombre', 'Descripcion')

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class ServiciosTiempo(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Servicio = models.ForeignKey(ServiciosExternosActividad)
    Descripcion = models.CharField(blank=True, max_length=100)
    Inmediatamente = models.NullBooleanField(default=False)
    Hora_1 = models.NullBooleanField(default=False)
    Hora_3 = models.NullBooleanField(default=False)
    Hora_6 = models.NullBooleanField(default=False)
    Hora_12 = models.NullBooleanField(default=False)
    Hora_24 = models.NullBooleanField(default=False)
    Mas_de_un_Dia = models.NullBooleanField(default=False)

    class Admin(admin.ModelAdmin):
        list_display = ('Servicio', 'Descripcion')
        search_fields = ('Servicio', 'Descripcion')

    def __unicode__(self):
        return u"%s %s" % (self.Servicio, self.Descripcion)

ImpactoCualitativo = (
    (0, 'Ninguno'),
    (2, 'Minimo'),
    (4, 'Moderado'),
    (6, 'Moderadamente Grave'),
    (8, 'Grave'),
    (10, 'Catastrofico'),
)


class RyLImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Descripcion = models.CharField(blank=True, max_length=100)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCualitativo)

    class Meta:
        verbose_name_plural = "Impactos Regulatororio y Legal"
        verbose_name = "Impacto Regulatorio y Legal"

    class Admin(admin.ModelAdmin):
        list_display = ('Descripcion', )
        search_fields = ('Descripcion', )

    def __unicode__(self):
        return u"%s" % (self.Descripcion)


class ServicioClienteImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia"""
    Descripcion = models.CharField(blank=True, max_length=100)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCualitativo)

    class Admin(admin.ModelAdmin):
        list_display = ('Descripcion', )
        search_fields = ('Descripcion', )

    def __unicode__(self):
        return u"%s" % (self.Descripcion)


class ImagenImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Descripcion = models.CharField(blank=True, max_length=100)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCualitativo)

    class Admin(admin.ModelAdmin):
        list_display = ('Descripcion', )
        search_fields = ('Descripcion', )

    def __unicode__(self):
        return u"%s" % (self.Descripcion)


class IngresosImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Descripcion = models.CharField(blank=True, max_length=100)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCuantitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCuantitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCuantitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCuantitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCuantitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCuantitativo)

    class Admin(admin.ModelAdmin):
        list_display = ('Descripcion',)
        search_fields = ('Descripcion',)

    def __unicode__(self):
        return u"%s" % (self.Descripcion)


class GastosImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Descripcion = models.CharField(blank=True, max_length=100)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCuantitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCuantitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCuantitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCuantitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCuantitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCuantitativo)

    class Admin(admin.ModelAdmin):
        list_display = ('Descripcion',)
        search_fields = ('Descripcion',)

    def __unicode__(self):
        return u"%s" % (self.Descripcion)


class AplicacionesImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Aplicacion = models.ForeignKey(activo)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCualitativo)
    Backup = models.NullBooleanField(default=False)
    Frecuencia_Backup = models.IntegerField(blank=True, null=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Aplicacion',)
        search_fields = ('Aplicacion',)

    def __unicode__(self):
        return u"%s" % (self.Aplicacion)


class DocumentoImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Documento = models.ForeignKey(DocumentosActividad)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCualitativo)
    Backup = models.NullBooleanField(default=False)
    Frecuencia_Backup = models.IntegerField(blank=True, null=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Documento',)
        search_fields = ('Documento',)

    def __unicode__(self):
        return u"%s" % (self.Documento)


class PapelImpacto(models.Model):
    """(PersonasTiempo description)"""
    """ modelo basico para almacenar los datos de personas y tiempos requeridos
    para atender una emergencia """
    Papel = models.ForeignKey(PapelActividad)
    Hora_1 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_3 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_6 = models.IntegerField(blank=True, null=True,
                                 choices=ImpactoCualitativo)
    Hora_12 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Hora_24 = models.IntegerField(blank=True, null=True,
                                  choices=ImpactoCualitativo)
    Mas_de_un_Dia = models.IntegerField(blank=True, null=True,
                                        choices=ImpactoCualitativo)
    Backup = models.NullBooleanField(default=False)
    Frecuencia_Backup = models.IntegerField(blank=True, null=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Papel',)
        search_fields = ('Papel',)

    def __unicode__(self):
        return u"%s" % (self.Papel)
Alternativa_1 = '¿Pueden otras actividades continuar con el funcionamiento' +\
                'de esta actividad? En caso afirmativo, ¿cuáles?'
Alternativa_2 = '¿Es posible realizar algunas actividades en forma manual, ' +\
                'sin equipos de TI ni de otro tipo?'
Experiencia_1 = '¿Con qué frecuencia se han producido incidentes disruptivos' +\
                'en el negocio hasta ahora? ¿Cuánto tiempo duraron?'
Experiencia_2 = '¿Cómo se manejaron esas situaciones?'


class Actividad(models.Model):
    """(Actividad description)"""
    """ Modelo basico para almacenar los datos para BIA de actividades de riesgo
    por proceso dentro de la empresa """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(blank=True, max_length=100)
    Proceso = models.ForeignKey(ProcesoBia)
    Fecha = models.DateField(default=datetime.datetime.today)
    Regulatorio_y_Legal = models.ManyToManyField(RyLImpacto, blank=True)
    Servicio_al_Cliente = models.ManyToManyField(ServicioClienteImpacto,
                                                 blank=True)
    Imagen_Reputacional = models.ManyToManyField(ImagenImpacto, blank=True)
    Perdida_de_Ingresos = models.ManyToManyField(IngresosImpacto, blank=True)
    Gastos_Adicionales = models.ManyToManyField(GastosImpacto, blank=True)
    Personas = models.ManyToManyField(PersonasTiempo, blank=True)
    Aplicaciones = models.ManyToManyField(AplicacionesTiempo, blank=True)
    Documentos = models.ManyToManyField(DocumentosTiempo, blank=True)
    Papel = models.ManyToManyField(PapelTiempo, blank=True)
    Equipos_Ti = models.ManyToManyField(EquiposTiTiempo, blank=True)
    Canales_de_Comunicacion = models.ManyToManyField(CanalesTiempo, blank=True)
    Instalaciones = models.ManyToManyField(InstalacionesTiempo, blank=True)
    Capital = models.ManyToManyField(CapitalTiempo, blank=True)
    Servicios_Externos = models.ManyToManyField(ServiciosTiempo, blank=True)
    Dependencia_Organizacion = models.TextField(blank=True, null=True,
                                                verbose_name='Dependencia de' +
                                                ' otras areas de la ' +
                                                'Organizacion')
    Dependencia_de_Socios = models.TextField(blank=True, null=True)
    Dependencia_de_Proveedores = models.TextField(blank=True, null=True)
    Perdida_Aplicacion = models.ManyToManyField(AplicacionesImpacto,
                                                blank=True)
    Perdida_Documentos = models.ManyToManyField(DocumentoImpacto, blank=True)
    Perdida_Papel = models.ManyToManyField(PapelImpacto, blank=True)
    Alternativa1 = models.TextField(blank=True, null=True,
                                    verbose_name=Alternativa_1)
    Alternativa2 = models.TextField(blank=True, null=True,
                                    verbose_name=Alternativa_2)
    Experiencia1 = models.TextField(blank=True, null=True,
                                    verbose_name=Experiencia_1)
    Experiencia2 = models.TextField(blank=True, null=True,
                                    verbose_name=Experiencia_2)
    Comentario = models.TextField(blank=True, null=True)
    Conclusion = models.TextField()

    class Meta:
        verbose_name_plural = "Actividades"
        verbose_name = "Actividad"

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', 'Proceso', 'Fecha')
        search_fields = ('Nombre', 'Proceso',)
        fieldsets = [
            (None, {'fields': ['Nombre', 'Descripcion', 'Proceso',
                               'Fecha', ]}),
            ('Impactos Cualitativos', {'fields': ['Regulatorio_y_Legal',
                                                  'Servicio_al_Cliente',
                                                  'Imagen_Reputacional']}),
            ('Impactos Cuantitativos', {'fields': ['Perdida_de_Ingresos',
                                                   'Gastos_Adicionales', ]}),
            ('Recursos necesarios para la recuperación',
                {'fields': ['Personas', 'Aplicaciones', 'Documentos', 'Papel',
                            'Equipos_Ti', 'Canales_de_Comunicacion',
                            'Instalaciones', 'Capital',
                            'Servicios_Externos']}),
            ('Dependencia de terceros(quién es necesario para la recuperación'
                + 'de esta actividad)',
                {'fields': ['Dependencia_de_Socios',
                            'Dependencia_de_Proveedores',
                            'Dependencia_Organizacion']}),
            ('Pérdida máxima de datos:cantidad de datos que se pueden perder' +
             'basandose en la tabla de calificacion de perdida de datos',
             {'fields': ['Perdida_Aplicacion', 'Perdida_Documentos',
                         'Perdida_Papel', ]}),
            ('Alternativas en el caso de un desastre',
                {'fields': ['Alternativa1', 'Alternativa2']}),
            ('Experiencias Anteriores', {'fields': ['Experiencia1',
                                                    'Experiencia2']}),
            (None, {'fields': ['Comentario', 'Conclusion']}), ]

    def __unicode__(self):
        return u"%s" % (self.Nombre)
