from django.db import models

from apps.solicitante.models import Domicilio
from apps.solicitante.models import Telefono


class Comedor(models.Model):
    nombre = models.CharField(u'nombre', max_length=50)
    telefono_fk = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    domicilio_fk = models.ForeignKey(Domicilio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


