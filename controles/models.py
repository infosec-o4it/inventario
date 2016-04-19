from django.db import models


# Create your models here.
class Metodologia(models.Model):
    nombre = models.CharField(max_length=10)

    def __unicode__(self):
        return str(self.nombre)


class Dominio(models.Model):
    nombre = models.CharField(max_length=60)
    metodologia = models.ForeignKey(Metodologia)

    def __unicode__(self):
        return str(self.nombre + " " + str(self.metodologia))


class Control(models.Model):
    nombre = models.CharField(max_length=60)
    dominio = models.ForeignKey(Dominio)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "controles"

    def __unicode__(self):
        return str(self.nombre.encode("utf8") + " " + str(self.dominio))


class Registro(models.Model):
    control = models.ForeignKey(Control)
    fecha = models.DateField()
    resultado = models.TextField(null=True, blank=True)
    # soporte = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return str(str(self.control) + " " + str(self.fecha))


class Grado(models.Model):
    nombre = models.CharField(max_length=60)

    def __unicode__(self):
        return str(self.nombre)


class Madurez(models.Model):
    grado = models.ForeignKey(Grado)
    fecha = models.DateField()
    registro = models.ForeignKey(Registro)

    class Meta:
        verbose_name_plural = "niveles de madurez"

    def __unicode__(self):
        return str(
            str(self.grado) +
            " " +
            str(self.fecha) +
            " " +
            str(self.registro)
        )
