from django.db import models

# Create your models here.
class tipo(models.Model):
    tipo = models.CharField(max_length=30)
    def __unicode__(self):
        return self.tipo
    
class area(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return unicode(self.nombre)
    
class usuario(models.Model):
    cargo = models.CharField(max_length=40)
    telefono = models.CharField(max_length=12)
    area = models.ForeignKey(area)
    def __unicode__(self):
        return unicode(self.cargo)
    
class activo(models.Model):
    activo = models.CharField(max_length=30)
    descripcion = models.TextField(null=True,blank=True)
    tipo = models.ForeignKey(tipo)
    ubicacion = models.CharField(max_length=30,null=True, blank=True)
    area = models.ForeignKey(area) 
    propietario = models.ForeignKey(usuario, related_name = "propietario")
    responsable = models.ForeignKey(usuario, related_name = "responsable")
    usuario = models.ForeignKey(usuario)
    funcion = models.TextField(null=True, blank=True)
    datos_personales = models.NullBooleanField()
    propia = models.NullBooleanField()
    terceros = models.NullBooleanField()
    clientes = models.NullBooleanField()
    def __unicode__(self):
        return self.activo

class niveles_acceso(models.Model):
    activo = models.ForeignKey(activo)
    usuario = models.ForeignKey(usuario) 
    leer = models.NullBooleanField()
    modificar = models.NullBooleanField()
    borrar = models.NullBooleanField()
    unique_together = (activo,usuario)      
