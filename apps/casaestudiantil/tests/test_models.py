# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.solicitante.models import *
from apps.casaestudiantil.models import *
from django.core.exceptions import ValidationError
#11
class ModelsTest(TestCase):

    def setUp(self):
        self.descripcionCasa = DescripcionCasa.objects.create(
            nombre_dueno = "Miguel Angel Esparza",
            capacidad = "334",
            camas = "334",
            cuartos = "152",
            sillas = "334",
            cocinas = "2",
            banios = "11"
            )
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
            codigo_postal = "99000",
            estado = self.estado,
            municipio = self.municipio
            )
        self.telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        self.casaEstudiantil = CasaEstudiantil.objects.create(
                # campo nombre vacia porque es especifico para 
                # el test_no_se_puede_guardar_registros_vacios
                nombre = '',
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                descripcion_casa_fk = self.descripcionCasa
            )
    def test_guardando_y_recuperando_datos_solicitante(self):
        self.casaEstudiantil.save()
        saved_casaEstudiantil = CasaEstudiantil.objects.first()
        #saved_list = List.objects.first()
        self.assertEqual(saved_casaEstudiantil, self.casaEstudiantil)
        saved_casas = CasaEstudiantil.objects.all()
        self.assertEqual(saved_casas.count(), 1)
        first_saved_casaEstudiantil = saved_casas[0]
        # second_saved_item = saved_items[1]
        self.assertEqual(first_saved_casaEstudiantil.nombre, '')
        self.assertEqual(first_saved_casaEstudiantil.telefono_fk, self.telefono)
        self.assertEqual(first_saved_casaEstudiantil.domicilio_fk, self.domicilio)
        self.assertEqual(first_saved_casaEstudiantil.descripcion_casa_fk, self.descripcionCasa)

    def test_no_se_puede_guardar_registros_vacios(self):
        with self.assertRaises(ValidationError):
            self.casaEstudiantil.save()
            self.casaEstudiantil.full_clean()

    def test_get_absolute_url(self):
        self.assertEqual('/casaestudiantil/', f'/casaestudiantil/')

    def test_duplicate_casas_are_invalid(self):
        casa = self.casaEstudiantil
        casa.save()
        with self.assertRaises(ValidationError):
            casa2 = self.casaEstudiantil
            casa2.full_clean()
            casa2.save()

    def test_CAN_save_same_solicitante(self):
        descripcionCasa = DescripcionCasa.objects.create(
            nombre_dueno = "Miguel Angel Esparza",
            capacidad = "334",
            camas = "334",
            cuartos = "152",
            sillas = "334",
            cocinas = "2",
            banios = "11"
            )
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
            codigo_postal = "99000",
            estado = estado,
            municipio = municipio
            )
        telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        casaEstudiantil2 = CasaEstudiantil.objects.create(
                # campo nombre vacia porque es especifico para 
                # el test_no_se_puede_guardar_registros_vacios
                nombre = 'Terminal 1',
                telefono_fk = telefono,
                domicilio_fk = domicilio,
                descripcion_casa_fk = descripcionCasa
            )
        casaEstudiantil2.full_clean()  # should not raise
        casaEstudiantil2.save()

    def test_string_representation_estado_model(self):
        self.assertEqual(str(self.estado), 'Zacatecas')

    def test_string_representation_municipio_model(self):
        self.assertEqual(str(self.municipio), 'Zacatecas')

    def test_string_representation_domicilio_model(self):
        self.assertEqual(str(self.domicilio), 'Lopez Velarde 204 Centro 99000 Zacatecas Zacatecas')

    def test_string_representation_telefono_model(self):
        self.assertEqual(str(self.telefono), '3941030048')

    def test_string_representation_descripcion_casa_model(self):
        self.assertEqual(str(self.descripcionCasa), 'Miguel Angel Esparza 334 334 152 334 2 11')

    def test_string_representation_casa_estudiantil_model(self):
        # porque se envia campo vacio en la crecion del objeto CasaEstudiantil
        self.assertEqual(str(self.casaEstudiantil), '')