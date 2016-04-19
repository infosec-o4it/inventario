# -*- coding: utf-8 -*-
from django.db import models
from informacion.models import usuario
# Create your models here.


class seccion(models.Model):
    codigo = models.CharField(max_length=4)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "secciones"

    def __unicode__(self):
        return u'%s' % (self.codigo.encode("utf8"))


class control(models.Model):
    seccion = models.ForeignKey(seccion)
    codigo = models.CharField(max_length=3)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "controles"

    def __unicode__(self):
        return u'%s.%s' % (self.seccion, self.codigo)


class numeral(models.Model):
    control = models.ForeignKey(control)
    codigo = models.CharField(max_length=3)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "numerales"

    def __unicode__(self):
        return u'%s.%s' % (self.control, self.codigo)


class punto(models.Model):
    numeral = models.ForeignKey(numeral)
    pregunta = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.numeral, self.pregunta[:35])
nivel = (
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


class hallazgo(models.Model):
    punto = models.ForeignKey(punto)
    resumen = models.CharField(max_length=16)
    usuario = models.ForeignKey(usuario)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateField()
    nota = models.IntegerField(choices=nivel)

    def __unicode__(self):
        return u'%s - respuesta: %s' % (self.punto, self.resumen)
