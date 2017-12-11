# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.supervisor.models import Supervisor
from apps.casaestudiantil.models import CasaEstudiantil, DescripcionCasa
from apps.comedor.models import Comedor
from apps.solicitante.models import Domicilio
from apps.solicitante.models import Municipio
from apps.solicitante.models import Estado
from apps.solicitante.models import Telefono

from apps.solicitante.forms import DomicilioForm
from apps.solicitante.forms import TelefonoForm
from apps.supervisor.forms import SupervisorForm


class AllFormsTest(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(
            estado="Zacatecas"
        )
        self.municipio = Municipio.objects.create(
            municipio="Zacatecas",
            estado_fk=self.estado
        )
        self.descripcion_casa = DescripcionCasa.objects.create(
            nombre_dueno='CASE',
            capacidad=50,
            camas=30,
            cuartos=15,
            sillas=50,
            cocinas=2,
            banios=5,
        )
        self.casa_estudiantil = CasaEstudiantil.objects.create(
            nombre='MODULO A',
            domicilio_fk=Domicilio.objects.create(
                numero='204',
                calle='Preparatoria',
                colonia="Hidraulica",
                codigo_postal="98000",
                estado=self.estado,
                municipio=self.municipio,
            ),
            telefono_fk=Telefono.objects.create(
                telefono="4921008989",
                tipo='FIJO'
            ),
            descripcion_casa_fk = self.descripcion_casa,
        )
        self.comedor = Comedor.objects.create(
            nombre="INGENIERIA",
            domicilio_fk=Domicilio.objects.create(
                numero='204',
                calle='Preparatoria',
                colonia="Hidraulica",
                codigo_postal="98000",
                estado=self.estado,
                municipio=self.municipio,
            ),
            telefono_fk=Telefono.objects.create(
                telefono="4921007789",
                tipo='FIJO',
            ),
        )

        self.supervisor = Supervisor.objects.create(
            nombre='Pablo Cesar',
            apellido_paterno="Rodriguez",
            apellido_materno="Aguayo",
            comedor_fk=self.comedor,
            casas_estudiantil_fk=self.casa_estudiantil,
        )

    def test_form_telefono_input_has_css_classes(self):
        form = TelefonoForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_domicilio_input_has_css_classes(self):
        form = DomicilioForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_blank_items_telefono_form(self):
        form = TelefonoForm(data={'telefono': '', 'tipo': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['telefono'],
                         ['This field is required.'])
        self.assertEqual(form.errors['tipo'],
                         ['This field is required.'])

    def test_form_validation_for_blank_items_domicilio_form(self):
        form = DomicilioForm(data={
            'numero': '',
            'calle': '',
            'colonia': '',
            'codigo_postal': '',
            'estado': '',
            'municipio': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['numero'],
                         ['This field is required.'])
        self.assertEqual(form.errors['calle'],
                         ['This field is required.'])
        self.assertEqual(form.errors['colonia'],
                         ['This field is required.'])
        self.assertEqual(form.errors['codigo_postal'],
                         ['This field is required.'])
        self.assertEqual(form.errors['estado'],
                         ['This field is required.'])
        self.assertEqual(form.errors['municipio'],
                         ['This field is required.'])

    def test_form_validation_for_blank_items_solicitante_form(self):
        form = SupervisorForm(data={
            'nombre': '',
            'apellido_paterno': '',
            'apellido_materno': '',})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nombre'],
                         ['This field is required.'])
        self.assertEqual(form.errors['apellido_paterno'],
                         ['This field is required.'])
        self.assertEqual(form.errors['apellido_materno'],
                         ['This field is required.'])

    def test_form_save_handles_saving_to_a_solicitante(self):
        supervisor = self.supervisor
        form = SupervisorForm(
            data={
                'nombre': 'Pablo Cesar',
                'apellido_paterno': 'Rodriguez',
                'apellido_materno': 'Aguayo'
            }
        )
        self.assertEqual(supervisor, Supervisor.objects.first())
        self.assertEqual(supervisor.nombre, 'Pablo Cesar')
        self.assertEqual(supervisor.apellido_paterno, 'Rodriguez')
        self.assertEqual(supervisor.apellido_materno, 'Aguayo')

