# -*- coding: utf-8 -*-
from django.test import TestCase

from apps.supervisor.models import Supervisor
from apps.casaestudiantil.models import CasaEstudiantil
from apps.casaestudiantil.models import DescripcionCasa
from apps.comedor.models import Comedor

from apps.solicitante.models import Domicilio
from apps.solicitante.models import Municipio
from apps.solicitante.models import Estado
from apps.solicitante.models import Telefono

from django.core.exceptions import ValidationError


class ModelsTest(TestCase):
    def setUp(self):
        self.estado = Estado.objects.create(
            estado="Zacatecas"
        )
        self.municipio = Municipio.objects.create(
            municipio="Zacatecas",
            estado_fk=self.estado,
        )
        self.domicilio = Domicilio.objects.create(
            numero='311',
            calle='Preparatoria',
            colonia="Centro",
            codigo_postal="98000",
            estado=self.estado,
            municipio=self.municipio,
        )
        self.domicilio_casa = Domicilio.objects.create(
            numero='311',
            calle='Preparatoria',
            colonia="Centro",
            codigo_postal="98000",
            estado=self.estado,
            municipio=self.municipio,
        )
        self.telefono = Telefono.objects.create(
            telefono="4921001212",
            tipo="FIJO",
        )
        self.telefono_casa = Telefono.objects.create(
            telefono="4921011112",
            tipo="FIJO",
        )
        self.comedor = Comedor.objects.create(
            nombre="INGENIERIA",
            telefono_fk=self.telefono,
            domicilio_fk=self.domicilio,
        )

        self.descripcion_casa = DescripcionCasa.objects.create(
            nombre_dueno="CASE UAZ",
            capacidad = 100,
            camas = 50,
            cuartos = 15,
            sillas = 5,
            cocinas = 3,
            banios = 5,
        )

        self.casa_estudiantil = CasaEstudiantil.objects.create(
            nombre="MODULO A",
            telefono_fk=self.telefono_casa,
            domicilio_fk=self.domicilio_casa,
            descripcion_casa_fk=self.descripcion_casa,
        )
        self.supervisor = Supervisor.objects.create(
            nombre='',  # se modifica este campo para la pruea test_cannot
            apellido_paterno="Rodriguez",
            apellido_materno="Aguayo",
            comedor_fk=self.comedor,
            casas_estudiantil_fk=self.casa_estudiantil,
        )


    def test_guardando_y_recuperando_datos_supervisor(self):
        self.supervisor.save()
        saved_supervisor = Supervisor.objects.first()
        self.assertEqual(saved_supervisor, self.supervisor)
        saved_supervisores = Supervisor.objects.all()
        self.assertEqual(saved_supervisores.count(), 1)
        first_saved_supervisor = saved_supervisores[0]
        self.assertEqual(first_saved_supervisor.nombre,
                         '')
        self.assertEqual(first_saved_supervisor.apellido_paterno,
                         'Rodriguez')
        self.assertEqual(first_saved_supervisor.apellido_materno,
                         'Aguayo')
        self.assertEqual(first_saved_supervisor.comedor_fk.telefono_fk,
                         self.telefono)
        self.assertEqual(first_saved_supervisor.comedor_fk.domicilio_fk,
                         self.domicilio)

        self.assertEqual(first_saved_supervisor.casas_estudiantil_fk.telefono_fk,
                         self.telefono_casa)
        self.assertEqual(first_saved_supervisor.casas_estudiantil_fk.domicilio_fk,
                         self.domicilio_casa)

    def test_no_se_puede_guardar_registros_vacios(self):
        with self.assertRaises(ValidationError):
            self.supervisor.save()
            self.supervisor.full_clean()

    def test_get_absolute_url(self):
        self.assertEqual('/supervisor/', u'/supervisor/')

    def test_duplicate_items_are_invalid(self):
        supervisor = self.supervisor
        with self.assertRaises(ValidationError):
            supervisor = self.supervisor
            supervisor.full_clean()
            supervisor.save()



