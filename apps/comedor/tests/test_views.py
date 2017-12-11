from django.test import TestCase
from apps.comedor.models import *
from apps.solicitante.models import *
from apps.comedor.forms import *
# 17 pruebas unitarias
class ComedorPageTest(TestCase):

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
                nombre = "Jesús Pérez Cuevas (Ingenierías)",
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio
                )
    def test_comedor_nuevo_template(self):
        response = self.client.get('/comedor/nuevo')
        self.assertTemplateUsed(response, 'comedor/comedor_form.html')

    def test_comedor_mostrar_template(self):
        response = self.client.get('/comedor/mostrar')
        self.assertTemplateUsed(response, 'comedor/comedor_list.html')

    def test_comedor_editar_template(self):
        response = self.client.get(f'/comedor/editar/{self.comedor.id}/')
        self.assertTemplateUsed(response, 'comedor/comedor_form.html')

    def test_comedor_delete_template(self):
        response = self.client.get(f'/comedor/eliminar/{self.comedor.id}/')
        self.assertTemplateUsed(response, 'comedor/comedor_delete.html')

    '''
    PAGES USES FORM {}
    '''
    def test_comedor_nuevo_page_uses_comedor_form(self):
        response = self.client.get('/comedor/nuevo')
        self.assertIsInstance(response.context['form_comedor'], ComedorForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
        
    
    def test_comedor_editar_page_uses_actualizar_comedor_form(self):
        response = self.client.get(f'/comedor/editar/{self.comedor.id}/')
        self.assertIsInstance(response.context['form_comedor'], ComedorForm)        
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
    '''
    PAGES USES FORM {}
    '''

class EditSolicitantesTest(TestCase):

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
            nombre = "Jesús Pérez Cuevas (Ingenierías)",
            telefono_fk = self.telefono,
            domicilio_fk = self.domicilio
            )

    def test_uses_edit_template(self):
        comedor = self.comedor
        response = self.client.get(f'/comedor/editar/{comedor.id}/')
        self.assertTemplateUsed(response, 'comedor/comedor_form.html')

     
    def test_displays_actualizar_comedor_form(self):
        comedor = self.comedor
        response = self.client.get(f'/comedor/editar/{comedor.id}/')
        self.assertIsInstance(response.context['form_comedor'], ComedorForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
        self.assertContains(response, 'name="nombre"')
        self.assertContains(response, 'name="numero"')
        self.assertContains(response, 'name="calle"')
        self.assertContains(response, 'name="colonia"')
        self.assertContains(response, 'name="codigo_postal"')
        self.assertContains(response, 'name="estado"')
        self.assertContains(response, 'name="municipio"')
        self.assertContains(response, 'name="telefono"')

    def test_delete_only_for_that_solicitante(self):
        estado = Estado.objects.create(
            estado = "Zacatecas"
            )
        municipio = Municipio.objects.create(
            municipio = "Zacatecas",
            estado_fk = estado
            )
        domicilio = Domicilio.objects.create(
            numero = '204',
            calle = 'Siglo XXI',
            colonia = "El Ejidal",
            codigo_postal = "98000",
            estado = estado,
            municipio = municipio
            )
        telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        comedor2 = Comedor.objects.create(
            nombre = "Siglo XXI",
            telefono_fk = telefono,
            domicilio_fk = domicilio
            )

        correct_comedor = self.comedor
        other_comedor = comedor2
        response = self.client.get(f'/comedor/editar/{correct_comedor.id}/')
        self.assertContains(response, 'Jesús Pérez Cuevas (Ingenierías)')
        self.assertNotContains(response, 'Siglo XXI')

class DeleteSolicitantesTest(TestCase):

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
            nombre = "Jesús Pérez Cuevas (Ingenierías)",
            telefono_fk = self.telefono,
            domicilio_fk = self.domicilio
            )

    def test_uses_delete_template(self):
        comedor = self.comedor
        response = self.client.get(f'/comedor/eliminar/{comedor.id}/')
        self.assertTemplateUsed(response, 'comedor/comedor_delete.html')
     
    def test_displays_delete_comedor_form(self):
        comedor = self.comedor
        response = self.client.get(f'/comedor/eliminar/{comedor.id}/')
        self.assertContains(response, 'name="author"')

    def test_delete_only_for_that_comedor(self):
        estado = Estado.objects.create(
            estado = "Zacatecas"
            )
        municipio = Municipio.objects.create(
            municipio = "Zacatecas",
            estado_fk = estado
            )
        domicilio = Domicilio.objects.create(
            numero = '204',
            calle = 'Siglo XXI',
            colonia = "El Ejidal",
            codigo_postal = "98000",
            estado = estado,
            municipio = municipio
            )
        telefono = Telefono.objects.create(
            telefono = "3941030048",
            tipo = "FIJO"
            )
        comedor2 = Comedor.objects.create(
            nombre = "Prepa II",
            telefono_fk = telefono,
            domicilio_fk = domicilio
            )
        correct_comedor = self.comedor
        other_comedor = comedor2
        response = self.client.get(f'/comedor/eliminar/{correct_comedor.id}/')
        self.assertContains(response, 'Jesús Pérez Cuevas (Ingenierías)')
        self.assertNotContains(response, 'Prepa II')

class URLsTest(TestCase):

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
                nombre = "Jesús Pérez Cuevas (Ingenierías)",
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio
                )

    def test_root_url_resolves_to_mostrar_comedor_function(self):
        # Verfica si existe la url de comedor/mostrar
        response = self.client.get('/comedor/mostrar')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Listado Comedores')

    def test_root_url_resolves_to_login_function(self):
        # Verfica si existe la url de inicio sesion
        response = self.client.get('/',)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inicio Sesión')

    def test_root_url_resolves_to_comedor_nuevo_function(self):
        # Verfica si existe la url de comedor/nuevo
        response = self.client.get('/comedor/nuevo')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Formulario Comedor')

    def test_root_url_resolves_to_comedor_editar_function(self):
        # Verfica si existe la url de comedor/editar
        response = self.client.get(f'/comedor/editar/{self.comedor.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Formulario Comedor')

    def test_root_url_resolves_to_comedor_eliminar_function(self):
        # Verfica si existe la url de comedor/eliminar
        response = self.client.get(f'/comedor/eliminar/{self.comedor.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Elimiar Comedor')