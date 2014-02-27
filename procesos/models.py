from django.db import models

# Create your models here.


class area(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return unicode(self.nombre)
       
class persona(models.Model):
    cargo = models.CharField(max_length=40)
    telefono = models.CharField(max_length=12)
    area = models.ForeignKey(area)
    def __unicode__(self):
        return unicode(self.cargo)
    
class proceso(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    responsable = models.ForeignKey(persona)
    def __unicode__(self):
        return unicode(self.nombre)

class tipo(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return unicode(self.nombre)

class entrada(models.Model):
    tipo = models.ForeignKey(tipo)
    descripcion = models.TextField(null=True, blank=True)
    proceso = models.ForeignKey(proceso)
    es_salida = models.NullBooleanField(null=True, blank=True)
    def __unicode__(self):
        return unicode(self.descripcion)
    
class salida(models.Model):
    tipo = models.ForeignKey(tipo)
    descripcion = models.TextField(null=True, blank=True)
    proceso = models.ForeignKey(proceso)
    es_entrada = models.NullBooleanField(null=True, blank=True)
    def __unicode__(self):
        return unicode(self.descripcion)
    
class procedimiento(models.Model):
    proceso = models.ForeignKey(proceso)
    nombre = models.CharField(max_length=40) 
    descripcion = models.TextField(null=True, blank=True)
    entrada = models.ForeignKey(entrada)
    salida = models.ForeignKey(salida)
    area = models.ForeignKey(area)
    def __unicode__(self):
        return unicode(self.nombre)

class actividad(models.Model):
    nombre = models.CharField(max_length=40) 
    descripcion = models.TextField(null=True, blank=True)
    procedimiento = models.ForeignKey(procedimiento)
    class Meta:
        verbose_name_plural = "actividades"
    def __unicode__(self):
        return unicode(self.nombre)
