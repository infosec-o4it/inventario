from django.db import models

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
        return str(self.cargo)
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


class datacenter(models.Model):
    descripcion = models.CharField(max_length=10, choices=datacenters)

    def __unicode__(self):
        return str(self.descripcion)


class activo(models.Model):
    activo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    tipo = models.ForeignKey(tipo)
    ubicacion = models.ManyToManyField(datacenter)
    area = models.ForeignKey(area)
    propietario = models.ForeignKey(usuario, related_name="propietario")
    responsable = models.ForeignKey(usuario, related_name="responsable")
    usuario = models.ForeignKey(usuario)
    funcion = models.TextField(null=True, blank=True)
    datos_personales = models.NullBooleanField()
    propia = models.NullBooleanField()
    terceros = models.NullBooleanField()
    clientes = models.NullBooleanField()
    confidencialidad = models.IntegerField(choices=niveles, default=5)
    integridad = models.IntegerField(choices=niveles, default=5)
    disponibilidad = models.IntegerField(choices=niveles, default=5)

    def __unicode__(self):
        return self.activo


class niveles_acceso(models.Model):
    activo = models.ForeignKey(activo)
    usuario = models.ForeignKey(usuario)
    leer = models.NullBooleanField()
    modificar = models.NullBooleanField()
    borrar = models.NullBooleanField()
    unique_together = (activo, usuario)
