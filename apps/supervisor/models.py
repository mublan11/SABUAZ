from django.db import models

from apps.casaestudiantil.models import CasaEstudiantil
from apps.comedor.models import Comedor


class Supervisor(models.Model):
    nombre = models.CharField(
        u'nombre', max_length=50)
    apellido_paterno = models.CharField(
        u'apellido_paterno', max_length=50)
    apellido_materno = models.CharField(
        u'apellido_materno', max_length=50, null=True)
    comedor_fk = models.ForeignKey(Comedor)
    casas_estudiantil_fk = models.ForeignKey(CasaEstudiantil)

    def __str__(self):
        return "{0} {1} {2}".format(
            self.nombre,
            self.apellido_paterno,
            self.apellido_materno)
