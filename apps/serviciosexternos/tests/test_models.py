from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
from apps.serviciosexternos.models import ServiciosExternos


class ModelServiciosExternosTextCase(TestCase):

    def setUp(self):
        self.servicios_externos1 = ServiciosExternos.objects.create(
            nombre="Capacitacion Industrial Electronica",
            descripcion="Curso de ingeniería aplicada a los procesos de cableado industrial.",
            tipo='BECA',
            organizacion='OTRO',
            created_at=models.DateTimeField(auto_now=True)
        ).save()
        self.servicios_externos = ServiciosExternos.objects.create(
            nombre="Capacitacion Minera Biotecnologica",
            descripcion = "Curso de biotecnologia aplicada a los procesos minero-metalúrgicos.",
            tipo = 'BECA',
            organizacion = 'OTRO',
            created_at = models.DateTimeField(auto_now=True)
        )

    def test_model_crear_servicio_externo(self):
        servicios_previo = ServiciosExternos.objects.count()
        self.servicios_externos.save()
        ServiciosExternos.objects.get(id=1).delete()
        new_servicios = ServiciosExternos.objects.count()
        self.assertNotEqual(servicios_previo, new_servicios)

    def test_model_regresa_to_string(self):
        self.assertEqual(str(self.servicios_externos),
                         "{0} {1} {2}".format(self.servicios_externos.nombre,
                                              self.servicios_externos.descripcion,
                                              self.servicios_externos.organizacion))
