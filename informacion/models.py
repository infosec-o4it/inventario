# -*- coding: utf-8 -*-
from django.db import models
from controles.models import Control
from django.contrib import admin
import datetime
# Create your models here.


class tipo(models.Model):
    tipo = models.CharField(max_length=30)

    def __unicode__(self):
        return self.tipo


class area(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.nombre)


class usuario(models.Model):
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    area = models.ForeignKey(area)

    def __unicode__(self):
        return u"%s" % (self.cargo)

niveles = (
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
)
datacenters = (
    ("TMBOG", "Terramar Bogota"),
    ("TMMiami", "Terramar Miami"),
    ("XO", "XO Comunications"),
    ("UNEMed", "Une Medellin"),
    ("CLL74", "Oficina calle 74"),
    ("OF Remotas", "Oficinas Remotas"),
    ("Externo", "Externo"),
)


class VulnerabilidadesActivo(models.Model):
    """(VulnerabilidadesActivo description)"""
    """modelo basico implementado para almecenar las Vulnerabilidades no
    tecnicas y no tecnicas de un activo"""
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True, blank=True)
    CVE = models.CharField(null=True, blank=True, max_length=100)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre', )
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Vulnerabilidades"
        verbose_name = "Vulnerabilidad"

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class AmenazasActivo(models.Model):
    """(AmenazasActivo description)"""
    """ modelo basico implementado para almacenar las amenazas tecnicas y no
    tecnicas de un activo """
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(null=True, blank=True)
    Intensidad = models.IntegerField(blank=True, null=True)
    Frecuencia = models.IntegerField(blank=True, null=True)

    class Admin(admin.ModelAdmin):
        list_display = ('Nombre',)
        search_fields = ('Nombre',)

    class Meta:
        verbose_name_plural = "Amenazas"
        verbose_name = "Amenaza"

    def __unicode__(self):
        return u"%s" % (self.Nombre)


class datacenter(models.Model):
    descripcion = models.CharField(max_length=10, choices=datacenters)

    def __unicode__(self):
        return str(self.descripcion)

sistemas = (
    ('WIN', 'Windows'),
    ('LIN', 'Linux'),
    ('EMB', 'Embebido'),
    ('NOA', 'No Aplica'),
    ('FOR', 'Fortinet'),
    ('WSA', 'Windows Server'),
)


class activo(models.Model):
    activo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    tipo = models.ForeignKey(tipo, default=10)
    sistema = models.CharField(
        max_length=3,
        choices=sistemas,
        blank=True,
        default='NOA'
        )
    ubicacion = models.ManyToManyField(datacenter)
    area = models.ForeignKey('informacion.area')
    propietario = models.ForeignKey('informacion.usuario',
                                    related_name="propietario",
                                    default=34, verbose_name="propietario",)
    responsable = models.ForeignKey('informacion.usuario', default=34,
                                    related_name="responsable")
    usuario = models.ForeignKey('informacion.usuario', default=34)
    # propietario = models.ForeignKey(usuario, default=34,
    #                                 verbose_name="propietario") jaja
    # responsable = models.ForeignKey(usuario, default=34)
    # usuario = models.ForeignKey(usuario, default=34)
    funcion = models.TextField(null=True, blank=True)
    datos_personales = models.NullBooleanField(
        verbose_name="Contiene datos personales", default=False)
    propia = models.NullBooleanField(default=False)
    terceros = models.NullBooleanField(default=False)
    clientes = models.NullBooleanField(default=False)
    confidencialidad = models.IntegerField(choices=niveles, default=5)
    integridad = models.IntegerField(choices=niveles, default=5)
    disponibilidad = models.IntegerField(choices=niveles, default=5)
    Riesgo = models.IntegerField(blank=True, null=True)
    Amenazas = models.ManyToManyField(AmenazasActivo, blank=True,
                                      related_name='Amenaza')
    Vulnerabilidades = models.ManyToManyField(VulnerabilidadesActivo,
                                              blank=True,
                                              related_name='Vulnerabilidad')
    # Controles = models.ForeignKey(Control, blank=True, null=True)
    Controles = models.ManyToManyField(Control, blank=True)

    def __unicode__(self):
        return u"%s" % (self.activo)

    # class Meta:
    #     abstract = True


class niveles_acceso(models.Model):
    activo = models.ForeignKey(activo)
    usuario = models.ForeignKey(usuario)
    leer = models.NullBooleanField()
    modificar = models.NullBooleanField()
    borrar = models.NullBooleanField()
    unique_together = (activo, usuario)

    class Meta:
        verbose_name_plural = "niveles de acceso"
        verbose_name = "un nivel de acceso"


numero_pasos = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
    (26, '26'),
    (27, '27'),
    (28, '28'),
    (29, '29'),
    (30, '30'),
    (31, '31'),
    (32, '32'),
    (33, '33'),
    (34, '34'),
    (35, '35'),
    (36, '36'),
    (37, '37'),
    (38, '38'),
    (39, '39'),
    (40, '40'),
)


class ActividadPasoHardneing(models.Model):
    """docstring for ActividadPasoHardneing clase creada con el objeto de
    documentar los pasos de hardening necesarios para gantizar los niveles
    de seguridad de un activo"""
    Sistema_Operativo = models.CharField(
        max_length=3,
        choices=sistemas,
        default='WSA'
        )
    Numero_Paso = models.IntegerField(
        choices=numero_pasos,
        default='0'
        )
    Activdad = models.CharField(blank=True, max_length=100)
    Descripcion_Paso = models.TextField(blank=True)
    unique_together = (("Sistema_Operativo", "Numero_Paso"),)

    class Meta:
        unique_together = (('Sistema_Operativo', 'Numero_Paso'), )
        verbose_name_plural = "Actividades de Hardening"
        verbose_name = "Paso de Hardening"

    def __unicode__(self):
        return u"%s %s" % (self.Sistema_Operativo, self.Numero_Paso)


class RevisionActivo(models.Model):
    """docstring for RevisionAct Modelo implementado para docuemtar la revision
    de la linea base de los activos que apliquen para Hardening"""
    Activo = models.ForeignKey(activo)
    Ip = models.GenericIPAddressField()
    Revisado = models.ForeignKey(usuario)
    Fecha = models.DateField(default=datetime.datetime.today)
    Pasos_Comprobados = models.ManyToManyField(ActividadPasoHardneing)

    class Meta:
        verbose_name_plural = "Revisiones de linea base de los Activos"
        verbose_name = "Revision de Activo"

    def __unicode__(self):
        return u"%s %s" % (self.Ip, self.Fecha)
