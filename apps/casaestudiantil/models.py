from django.db import models

from apps.solicitante.models import Domicilio
from apps.solicitante.models import Telefono


class DescripcionCasa(models.Model):
    nombre_dueno = models.CharField(u'nombre_dueno', max_length=50, null=True)
    capacidad = models.CharField(u'capacidad', max_length=5)
    camas = models.CharField(u'camas', max_length=5)
    cuartos = models.CharField(u'cuartos', max_length=5)
    sillas = models.CharField(u'sillas', max_length=5)
    cocinas = models.CharField(u'cocinas', max_length=5)
    banios = models.CharField(u'banios', max_length=5)

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.nombre_dueno, self.capacidad, self.camas,
                                             self.cuartos, self.sillas, self.cocinas, self.banios)

class CasaEstudiantil(models.Model):
    nombre = models.CharField(u'nombre', max_length=50)
    telefono_fk = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    domicilio_fk = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    descripcion_casa_fk = models.ForeignKey(DescripcionCasa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

