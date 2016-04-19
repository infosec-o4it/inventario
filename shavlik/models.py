
from django.db import models


class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % (self.nombre_cliente)


class OS(models.Model):
    nombre_os = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % (self.nombre_os)


class Dominio(models.Model):
    nombre_dominio = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % (self.nombre_dominio)


class Datacenter(models.Model):
    nombre_datacenter = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % (self.nombre_datacenter)


class Rol(models.Model):
    nombre_rol = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % (self.nombre_rol)


class Servidores(models.Model):
    hostname = models.CharField(max_length=60)
    ip = models.GenericIPAddressField()
    datacenter = models.ForeignKey(Datacenter)
    sistema_operativo = models.ForeignKey(OS)
    cliente = models.ForeignKey(Cliente)
    dominio = models.ForeignKey(Dominio)
    rol = models.ForeignKey(Rol)
    shavlik = models.BooleanField(default=False)
    fecha_programada = models.DateField(auto_now=False, auto_now_add=False,
                                        null=True, blank=True)
    fecha_parchado = models.DateField(auto_now=False, auto_now_add=False,
                                      null=True, blank=True)
    comentarios = models.TextField(max_length=300, blank=True)
