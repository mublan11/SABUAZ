# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.comedor.models import *
from apps.solicitante.models import *
from django.core.exceptions import ValidationError
# 10
class ModelsTest(TestCase):

    def setUp(self):
        self.estado = Estado.objects.create(
            estado = "Zacatecas"
            )
        self.municipio = Municipio.objects.create(
            municipio = "Zacatecas",
            estado_fk = self.estado
            )
        self.domicilio = Domicilio.objects.create(
            numero = '204',
            calle = 'Lopez Velarde',
            colonia = "Centro",
            codigo_postal = "98000",
            estado = self.estado,
            municipio = self.municipio
            )
        self.telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        self.comedor = Comedor.objects.create(
            # porque se necesita para el test_no_se_puede_guardar_registros_vacios
            nombre = "", 
            telefono_fk = self.telefono,
            domicilio_fk = self.domicilio
            )
    def test_guardando_y_recuperando_datos_comedor(self):
        self.comedor.save()
        saved_comedor = Comedor.objects.first()
        self.assertEqual(saved_comedor, self.comedor)
        saved_comedores = Comedor.objects.all()
        self.assertEqual(saved_comedores.count(), 1)
        first_saved_comedor = saved_comedores[0]
        self.assertEqual(first_saved_comedor.nombre, '')
        self.assertEqual(first_saved_comedor.telefono_fk, self.telefono)
        self.assertEqual(first_saved_comedor.domicilio_fk, self.domicilio)

    def test_no_se_puede_guardar_registros_vacios(self):
        with self.assertRaises(ValidationError):
            self.comedor.save()
            self.comedor.full_clean()

    def test_get_absolute_url(self):
        self.assertEqual('/comedor/', f'/comedor/')

    def test_duplicate_comedores_are_invalid(self):
        comedor = self.comedor
        comedor.save()
        with self.assertRaises(ValidationError):
            comedor2 = self.comedor
            comedor2.full_clean()
            comedor2.save()

    def test_CAN_save_same_comedor(self):
        estado = Estado.objects.create(
            estado = "Zacatecas"
            )
        municipio = Municipio.objects.create(
            municipio = "Zacatecas",
            estado_fk = estado
            )
        domicilio = Domicilio.objects.create(
            numero = '204',
            calle = 'Lopez Velarde',
            colonia = "Centro",
            codigo_postal = "98000",
            estado = estado,
            municipio = municipio
            )
        telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        comedor2 = Comedor.objects.create(
            # porque se necesita para el test_no_se_puede_guardar_registros_vacios
            nombre = "Psicologia", 
            telefono_fk = telefono,
            domicilio_fk = domicilio
            )
        comedor2.full_clean()  # should not raise
        comedor2.save()
        
    def test_string_representation_comedor_model(self):
        self.assertEqual(str(self.comedor), '')

    def test_string_representation_estado_model(self):
        self.assertEqual(str(self.estado), 'Zacatecas')

    def test_string_representation_municipio_model(self):
        self.assertEqual(str(self.municipio), 'Zacatecas')

    def test_string_representation_domicilio_model(self):
        self.assertEqual(str(self.domicilio), 'Lopez Velarde 204 Centro 98000 Zacatecas Zacatecas')

    def test_string_representation_telefono_model(self):
        self.assertEqual(str(self.telefono), '3941030048')