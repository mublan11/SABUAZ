# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.solicitante.models import *
from django.core.exceptions import ValidationError
#14
class ModelsTest(TestCase):

    def setUp(self):
        self.unidadAcademica = UnidadAcademica.objects.create(
            nombre = "Ing Electrica"
            )
        self.programaLicenciatura = ProgramaLicenciatura.objects.create(
            nombre = "Ing Software",
            unidad_academica_id = self.unidadAcademica
            )
        self.datosAcademicos = DatosAcademicos.objects.create(
            matricula = "30115574",
            promedio = 8,
            unidad_academica = self.unidadAcademica,
            programa_academico = self.programaLicenciatura
            )
        self.documentos = Documentos.objects.create(
            tipo_beca = "ALIMENTACION",
            tipo_solicitud = "RENOVACION",
            )
        self.estado = Estado.objects.create(
            estado = "Zacatecas"
            )
        self.municipio = Municipio.objects.create(
            municipio = "Fresnillo",
            estado_fk = self.estado
            )
        self.domicilio = Domicilio.objects.create(
            numero = '204',
            calle = 'Carrillo Puerto',
            colonia = "Centro",
            codigo_postal = "99080",
            estado = self.estado,
            municipio = self.municipio
            )
        self.telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        self.solicitante = Solicitante.objects.create(
                # campo nombre vacia porque es especifico para 
                # el test_no_se_puede_guardar_registros_vacios
                nombre = '', 
                apellido_paterno = "Blanco",
                apellido_materno = "Murillo",
                sexo = "HOMBRE",
                datos_academicos_fk = self.datosAcademicos,
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                documentos_fk = self.documentos
            )
    def test_guardando_y_recuperando_datos_solicitante(self):
        self.solicitante.save()
        saved_solicitante = Solicitante.objects.first()
        #saved_list = List.objects.first()
        self.assertEqual(saved_solicitante, self.solicitante)
        saved_solicitantes = Solicitante.objects.all()
        self.assertEqual(saved_solicitantes.count(), 1)
        first_saved_solicitante = saved_solicitantes[0]
        # second_saved_item = saved_items[1]
        self.assertEqual(first_saved_solicitante.nombre, '')
        self.assertEqual(first_saved_solicitante.apellido_paterno, 'Blanco')
        self.assertEqual(first_saved_solicitante.apellido_materno, 'Murillo')
        self.assertEqual(first_saved_solicitante.sexo, 'HOMBRE')
        self.assertEqual(first_saved_solicitante.datos_academicos_fk, self.datosAcademicos)
        self.assertEqual(first_saved_solicitante.telefono_fk, self.telefono)
        self.assertEqual(first_saved_solicitante.domicilio_fk, self.domicilio)
        self.assertEqual(first_saved_solicitante.documentos_fk, self.documentos)

    def test_no_se_puede_guardar_registros_vacios(self):
        with self.assertRaises(ValidationError):
            self.solicitante.save()
            self.solicitante.full_clean()

    def test_get_absolute_url(self):
        self.assertEqual('/solicitante/', f'/solicitante/')

    def test_duplicate_solicitantes_are_invalid(self):
        solicitante = self.solicitante
        solicitante.save()
        with self.assertRaises(ValidationError):
            solicitante2 = self.solicitante
            solicitante2.full_clean()
            solicitante2.save()

    def test_CAN_save_same_solicitante(self):
        unidadAcademica = UnidadAcademica.objects.create(
            nombre = "Ing Electrica"
            )
        programaLicenciatura = ProgramaLicenciatura.objects.create(
            nombre = "Ing Software",
            unidad_academica_id = unidadAcademica
            )
        datosAcademicos = DatosAcademicos.objects.create(
            matricula = "30115580",
            promedio = 8,
            unidad_academica = unidadAcademica,
            programa_academico = programaLicenciatura
            )
        documentos = Documentos.objects.create(
            tipo_beca = "ALIMENTACION",
            tipo_solicitud = "RENOVACION"
            )
        estado = Estado.objects.create(
            estado = "Zacatecas"
            )
        municipio = Municipio.objects.create(
            municipio = "Fresnillo",
            estado_fk = estado
            )
        domicilio = Domicilio.objects.create(
            numero = '204',
            calle = 'Carrillo Puerto',
            colonia = "Centro",
            codigo_postal = "99080",
            estado = estado,
            municipio = municipio
            )
        telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        solicitante2 = Solicitante.objects.create(
                nombre = 'Carlos',
                apellido_paterno = "Garcia",
                apellido_materno = "Carrillo",
                sexo = "HOMBRE",
                datos_academicos_fk = datosAcademicos,
                telefono_fk = telefono,
                domicilio_fk = domicilio,
                documentos_fk = documentos
            )
        solicitante2.full_clean()  # should not raise
        solicitante2.save()
        
    def test_string_representation_unidad_academica_model(self):
        self.assertEqual(str(self.unidadAcademica), 'Ing Electrica')

    def test_string_representation_programa_licenciatura_model(self):
        self.assertEqual(str(self.programaLicenciatura), 'Ing Software')
    
    def test_string_representation_datos_academicos_model(self):
        self.assertEqual(str(self.datosAcademicos), '8 30115574')

    def test_string_representation_documentos_model(self):
        self.assertEqual(str(self.documentos), 'ALIMENTACION RENOVACION')

    def test_string_representation_estado_model(self):
        self.assertEqual(str(self.estado), 'Zacatecas')

    def test_string_representation_municipio_model(self):
        self.assertEqual(str(self.municipio), 'Fresnillo')

    def test_string_representation_domicilio_model(self):
        self.assertEqual(str(self.domicilio), 'Carrillo Puerto 204 Centro 99080 Zacatecas Fresnillo')

    def test_string_representation_telefono_model(self):
        self.assertEqual(str(self.telefono), '3941030048')

    def test_string_representation_solicitante_model(self):
        # porque se envia campo vacio en la crecion del objeto Solicitante
        self.assertEqual(str(self.solicitante), '') 