from __future__ import unicode_literals
from django.db import models


ORGANIZACION = (
    ('BECA', 'BECA'),
    ('SEE', 'SEE'),
    ('INCUFIDEZ', 'INCUFIDEZ'),
    ('CEISPD', 'CEISPD'),
    ('DIF', 'DIF'),
    ('CAVIZ', 'CAVIZ'),
    ('VIFAC', 'VIFAC'),
    ('IJEZ', 'IJEZ'),
    ('INMUZA', 'INMUZA'),
    ('OTRO', 'OTRO'),
)

TIPO = (
    ('BECA', 'BECA'),
    ('SERVICIO', 'SERVICIO'),
    ('OTRO', 'OTRO'),
)


class ServiciosExternos(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    tipo = models.CharField(max_length=50, choices=TIPO)
    organizacion = models.CharField(max_length=50, choices=ORGANIZACION)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.nombre,
                                    self.descripcion,
                                    self.organizacion)
