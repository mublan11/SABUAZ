from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from apps.serviciosexternos.models import ServiciosExternos


class ViewServiciosExternosTextCase(TestCase):
    def setUp(self):
        self.servicios_externos = ServiciosExternos.objects.create(
            nombre="Capacitacion Minera Biotecnologica",
            descripcion = "Curso de biotecnologia aplicada a los procesos minero-metalúrgicos.",
            tipo = 'BECA',
            organizacion = 'OTRO',
            created_at = models.DateTimeField(auto_now=True)
        )
        self.client = APIClient()

        self.servicios_externos_json = {
            "nombre":"Capacitacion Industrial Electronica",
            "descripcion" :"Curso de ingeniería aplicada a los procesos de cableado industrial.",
            "tipo":'BECA',
            "organizacion":'OTRO'
        }
        self.response = self.client.post(
            reverse('create'),
            self.servicios_externos_json,
            format='json'
        )

    # def test_api_create_servicio_externo(self):
    #     new_client = APIClient()
    #     rest_service = new_client.get('/servicios/servicio/', kwargs={'pk':5}, format='json')
    #     self.assertEqual(rest_service.status_code, status.HTTP_403_FORBIDDEN)
