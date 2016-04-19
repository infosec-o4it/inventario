from django.db import models
import datetime
from informacion.models import usuario, datacenter, tipo
from procesos.models import proceso


# Create your models here.
class DisposicionElemento(models.Model):
    """(DisposicionElemento description)"""
    accion = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name_plural = "Disposiciones"
        verbose_name = "Disposicion"

    def __unicode__(self):
        return u'%s' % (self.accion)


class RetencionElemento(models.Model):
    """(RetencionElemento description)"""
    nombre = models.CharField(blank=True, max_length=100,
                              verbose_name="Descripcion del periodo")

    class Meta:
        verbose_name_plural = "Periodos de Retencion"

    def __unicode__(self):
        return u'%s' % (self.nombre)


class RecuperacionElemento(models.Model):
    """(ClasificacionElemento description)"""
    nombre = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name_plural = "Metodos de Recuperacion"

    def __unicode__(self):
        return u'%s' % (self.nombre)


class UbicacionElemento(models.Model):
    """(UbicacionElemento description)"""
    ruta = models.CharField(max_length=100)
    ubicacion = models.ForeignKey(datacenter)

    class Meta:
        verbose_name_plural = "Ubicaciones"

    def __unicode__(self):
        return u'%s en %s' % (self.ruta, self.ubicacion)


class RegistroElemento(models.Model):
    """(RegistroElemento description)"""
    codigo = models.CharField(max_length=26)  # posiblemente inutil
    nombre = models.CharField(max_length=100)
    responsable = models.ForeignKey(usuario)
    proceso = models.ForeignKey(proceso, default="34")
    tipo = models.ForeignKey(tipo)
    recuperacion = models.ForeignKey(RecuperacionElemento)
    disposicion = models.ForeignKey(DisposicionElemento, default="1")
    ubicacion = models.ForeignKey(UbicacionElemento)
    acceso = models.ForeignKey(usuario, default=34, related_name="acceso")
    retencion = models.ForeignKey(RetencionElemento)
    fecha_de_actualizacion = models.DateField(default=datetime.datetime.today)

    class Meta:
        verbose_name_plural = "Registros"

    def __unicode__(self):
        return u'%s - %s' % (self.codigo, self.nombre)
