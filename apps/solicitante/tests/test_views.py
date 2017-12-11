from django.test import TestCase
from apps.solicitante.models import *
from apps.solicitante.forms import *
# 17 pruebas unitarias
class SolicitantePageTest(TestCase):

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
    def test_solicitante_nuevo_template(self):
        response = self.client.get('/solicitante/nuevo')
        self.assertTemplateUsed(response, 'solicitante/solicitante_form.html')

    def test_solicitante_mostrar_template(self):
        response = self.client.get('/solicitante/mostrar')
        self.assertTemplateUsed(response, 'solicitante/solicitante_list.html')

    def test_solicitante_editar_template(self):
        response = self.client.get(f'/solicitante/editar/{self.solicitante.id}/')
        self.assertTemplateUsed(response, 'solicitante/solicitante_form.html')

    def test_solicitante_delete_template(self):
        response = self.client.get(f'/solicitante/eliminar/{self.solicitante.id}/')
        self.assertTemplateUsed(response, 'solicitante/solicitante_delete.html')

    '''
    PAGES USES FORM
    '''
    def test_solicitante_nuevo_page_uses_solicitante_form(self):
        response = self.client.get('/solicitante/nuevo')
        self.assertIsInstance(response.context['form_solicitante'], SolicitanteForm)
        self.assertIsInstance(response.context['form_datos_academicos'], DatosAcademicosForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
        self.assertIsInstance(response.context['form_documentos'], DocumentosForm)
    
    def test_solicitante_editar_page_uses_actualizar_solicitante_form(self):
        response = self.client.get(f'/solicitante/editar/{self.solicitante.id}/')
        self.assertIsInstance(response.context['form_solicitante'], ActualizarSolicitanteForm)
        self.assertIsInstance(response.context['form_datos_academicos'], DatosAcademicosForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
        self.assertIsInstance(response.context['form_documentos'], DocumentosForm)
    '''
    PAGES USES FORM
    '''

class EditSolicitantesTest(TestCase):

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
            tipo_solicitud = "RENOVACION"
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

    def test_uses_edit_template(self):
        solicitante = self.solicitante
        response = self.client.get(f'/solicitante/editar/{solicitante.id}/')
        self.assertTemplateUsed(response, 'solicitante/solicitante_form.html')

     
    def test_displays_actualizar_solicitante_form(self):
        solicitante = self.solicitante
        response = self.client.get(f'/solicitante/editar/{solicitante.id}/')
        self.assertIsInstance(response.context['form_solicitante'], ActualizarSolicitanteForm)
        self.assertIsInstance(response.context['form_datos_academicos'], DatosAcademicosForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
        self.assertIsInstance(response.context['form_documentos'], DocumentosForm)
        self.assertContains(response, 'name="nombre"')
        self.assertContains(response, 'name="apellido_paterno"')
        self.assertContains(response, 'name="apellido_materno"')
        self.assertContains(response, 'name="sexo"')
        self.assertContains(response, 'name="status"')
        self.assertContains(response, 'name="matricula"')
        self.assertContains(response, 'name="promedio"')
        self.assertContains(response, 'name="unidad_academica"')
        self.assertContains(response, 'name="programa_academico"')
        self.assertContains(response, 'name="telefono"')
        self.assertContains(response, 'name="tipo"')
        self.assertContains(response, 'name="numero"')
        self.assertContains(response, 'name="calle"')
        self.assertContains(response, 'name="colonia"')
        self.assertContains(response, 'name="codigo_postal"')
        self.assertContains(response, 'name="estado"')
        self.assertContains(response, 'name="municipio"')
        self.assertContains(response, 'name="tipo_beca"')
        self.assertContains(response, 'name="tipo_solicitud"')
        self.assertContains(response, 'name="estudio_socioeconomico"')
        self.assertContains(response, 'name="comprobante_ingresos"')
        self.assertContains(response, 'name="ine_padres"')
        self.assertContains(response, 'name="boleta_calificaciones"')
        self.assertContains(response, 'name="comprobante_inscripcion"')
        self.assertContains(response, 'name="carta_compromiso_padres"')
        self.assertContains(response, 'name="comprobante_solicitud_linea"')
    
    def test_delete_only_for_that_solicitante(self):
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
        correct_solicitante = self.solicitante
        other_solicitante = solicitante2
        response = self.client.get(f'/solicitante/editar/{correct_solicitante.id}/')
        self.assertContains(response, 'Diego')
        self.assertContains(response, 'Blanco')
        self.assertNotContains(response, 'Carlos')
        self.assertNotContains(response, 'Garcia')

class DeleteSolicitantesTest(TestCase):

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
                tipo_solicitud = "RENOVACION"
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

    def test_uses_delete_template(self):
        solicitante = self.solicitante
        response = self.client.get(f'/solicitante/eliminar/{solicitante.id}/')
        self.assertTemplateUsed(response, 'solicitante/solicitante_delete.html')
     
    def test_displays_delete_solicitante_form(self):
        solicitante = self.solicitante
        response = self.client.get(f'/solicitante/eliminar/{solicitante.id}/')
        self.assertContains(response, 'name="author"')

    def test_delete_only_for_that_solicitante(self):
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
        correct_solicitante = self.solicitante
        other_solicitante = solicitante2
        response = self.client.get(f'/solicitante/eliminar/{correct_solicitante.id}/')
        self.assertContains(response, 'Diego')
        self.assertNotContains(response, 'Carlos')

class URLsTest(TestCase):

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

    def test_root_url_resolves_to_login_function(self):
        # Verfica si existe la url de inicio sesion
        response = self.client.get('/',)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inicio Sesión')

    def test_root_url_resolves_to_beca_nuevo_ingreso_function(self):
        # Verfica si existe la url de solicitante/nuevo
        response = self.client.get('/solicitante/nuevo')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Formulario Solicitante')

    def test_root_url_resolves_to_mostrar_nuevo_ingreso_function(self):
        # Verfica si existe la url de solicitante/mostrar
        response = self.client.get('/solicitante/mostrar')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lista Solicitante')

    def test_root_url_resolves_to_comedor_editar_function(self):
        # Verfica si existe la url de solicitante/editar
        response = self.client.get(f'/solicitante/editar/{self.solicitante.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Formulario Solicitante')

    def test_root_url_resolves_to_comedor_eliminar_function(self):
        # Verfica si existe la url de solicitante/eliminar
        response = self.client.get(f'/solicitante/eliminar/{self.solicitante.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Eliminar Solicitante')