from django.test import TestCase
from apps.solicitante.models import *
from apps.solicitante.forms import *

class AllFormsTest(TestCase):
    # Se crea un solicitante
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
                nombre = 'Diego',
                apellido_paterno = "Blanco",
                apellido_materno = "Murillo",
                sexo = "HOMBRE",
                datos_academicos_fk = self.datosAcademicos,
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                documentos_fk = self.documentos
            )

    def test_form_solicitante_input_has_css_classes(self):
        form = SolicitanteForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_actualizar_solicitante_input_has_css_classes(self):
        form = ActualizarSolicitanteForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_datos_academicos_input_has_css_classes(self):
        form = DatosAcademicosForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_telefono_input_has_css_classes(self):
        form = TelefonoForm()
        self.assertIn('class="form-control"', form.as_p())
        
    def test_form_domicilio_input_has_css_classes(self):
        form = DomicilioForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_documentos_input_has_css_classes(self):
        form = DocumentosForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_blank_items_solicitante_form(self):
        form = SolicitanteForm(data={'nombre': '', 'apellido_paterno':'',
            'apellido_materno':'','sexo':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nombre'], ['This field is required.'])
        self.assertEqual(form.errors['apellido_paterno'], ['This field is required.'])
        self.assertEqual(form.errors['apellido_materno'], ['This field is required.'])
        self.assertEqual(form.errors['sexo'], ['This field is required.'])

    def test_form_validation_for_blank_items_solicitante_actualizar_form(self):
        form = ActualizarSolicitanteForm(data={'nombre': '', 'apellido_paterno':'',
            'apellido_materno':'','sexo':'', 'status':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nombre'], ['This field is required.'])
        self.assertEqual(form.errors['apellido_paterno'], ['This field is required.'])
        self.assertEqual(form.errors['apellido_materno'], ['This field is required.'])
        self.assertEqual(form.errors['sexo'], ['This field is required.'])        
        
    def test_form_validation_for_blank_items_datos_academicos_form(self):
        form = DatosAcademicosForm(data={
            'matricula': '', 'promedio':'',
            'unidad_academica':'','programa_academico':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['matricula'], ['This field is required.'])
        self.assertEqual(form.errors['promedio'], ['This field is required.'])
        self.assertEqual(form.errors['unidad_academica'], ['This field is required.'])
        self.assertEqual(form.errors['programa_academico'], ['This field is required.'])

    def test_form_validation_for_blank_items_telefono_form(self):
        form = TelefonoForm(data={'telefono': '', 'tipo':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['telefono'], ['This field is required.'])
        self.assertEqual(form.errors['tipo'], ['This field is required.'])

    def test_form_validation_for_blank_items_domicilio_form(self):
        form = DomicilioForm(data={'numero': '', 'calle':'',
            'colonia':'','codigo_postal':'', 'estado':'', 'municipio':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['numero'], ['This field is required.'])
        self.assertEqual(form.errors['calle'], ['This field is required.'])
        self.assertEqual(form.errors['colonia'], ['This field is required.'])
        self.assertEqual(form.errors['codigo_postal'], ['This field is required.'])
        self.assertEqual(form.errors['estado'], ['This field is required.'])
        self.assertEqual(form.errors['municipio'], ['This field is required.'])

    def test_form_validation_for_blank_items_documentos_form(self):
        form = DocumentosForm(data={'tipo_beca': '', 'tipo_solicitud':'',
            'estudio_socioeconomico':'','comprobante_ingresos':'', 'ine_padres':'',
            'boleta_calificaciones':'','comprobante_inscripcion':'',
            'carta_compromiso_padres':'','comprobante_solicitud_linea':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['tipo_beca'], ['This field is required.'])
        self.assertEqual(form.errors['tipo_solicitud'], ['This field is required.'])

    def test_form_validation_for_duplicate_solicitantes(self):
        solicitante = self.solicitante
        form = DatosAcademicosForm(data={
            'matricula': '30115574', 'promedio':'8',
            'unidad_academica':'Ing Electrica','programa_academico':'Ing Software'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['matricula'], ['Datos academicos with this Matricula already exists.'])

    def test_form_save_handles_saving_to_a_solicitante(self):
        solicitante = self.solicitante
        form = SolicitanteForm(data={'nombre': 'Diego', 'apellido_paterno':'Blanco',
            'apellido_materno':'Murillo','sexo':'HOMBRE'})
        solicitante.save()
        self.assertEqual(solicitante, Solicitante.objects.first())
        self.assertEqual(solicitante.nombre, 'Diego')
        self.assertEqual(solicitante.apellido_paterno, 'Blanco')
        self.assertEqual(solicitante.apellido_materno, 'Murillo')
        self.assertEqual(solicitante.sexo, 'HOMBRE')

    def test_form_save(self):
        solicitante = self.solicitante
        form = SolicitanteForm(data={'nombre': 'Diego', 'apellido_paterno':'Blanco',
            'apellido_materno':'Murillo','sexo':'HOMBRE',
            'datos_academicos_fk':self.datosAcademicos,'telefono_fk': self.telefono,
            'domicilio_fk': self.telefono, 'documentos_fk':self.documentos})
        nuevo_solicitante = solicitante
        self.assertEqual(nuevo_solicitante, Solicitante.objects.all()[0])