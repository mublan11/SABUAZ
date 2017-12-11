from django.test import TestCase
from apps.solicitante.models import *
from apps.casaestudiantil.models import *
from apps.casaestudiantil.forms import *
# 17 pruebas unitarias
class CasaEstudiantilPageTest(TestCase):

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
                nombre = 'Frida Kahlo',
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                descripcion_casa_fk = self.descripcionCasa
            )
    def test_casa_estudiantil_nueva_template(self):
        response = self.client.get('/casaestudiantil/nuevo')
        self.assertTemplateUsed(response, 'casaestudiantil/casaestudiantil_form.html')

    def test_casa_estudiantil_mostrar_template(self):
        response = self.client.get('/casaestudiantil/mostrar')
        self.assertTemplateUsed(response, 'casaestudiantil/casaestudiantil_list.html')

    def test_casa_estudiantil_editar_template(self):
        response = self.client.get(f'/casaestudiantil/editar/{self.casaEstudiantil.id}/')
        self.assertTemplateUsed(response, 'casaestudiantil/casaestudiantil_form.html')

    def test_casa_estudiantil_delete_template(self):
        response = self.client.get(f'/casaestudiantil/eliminar/{self.casaEstudiantil.id}/')
        self.assertTemplateUsed(response, 'casaestudiantil/casaestudiantil_delete.html')

    '''
    PAGES USES FORM
    '''
    #casa_estudiantil
    def test_casa_estudiantil_page_uses_casa_estudiantil_form(self):
        response = self.client.get('/casaestudiantil/nuevo')
        self.assertIsInstance(response.context['form_casa_estudiantil'], CasaEstudiantilForm)
        self.assertIsInstance(response.context['form_descripcion_casa'], DescripcionCasaForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
    
    def test_casa_estudiantil_editar_page_uses_actualizar_casa_estudiantil_form(self):
        response = self.client.get(f'/casaestudiantil/editar/{self.casaEstudiantil.id}/')
        self.assertIsInstance(response.context['form_casa_estudiantil'], CasaEstudiantilForm)
        self.assertIsInstance(response.context['form_descripcion_casa'], DescripcionCasaForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
    '''
    PAGES USES FORM
    '''
class EditCasaEstudiantilTest(TestCase):

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
                nombre = 'Frida Kahlo',
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                descripcion_casa_fk = self.descripcionCasa
            )

    def test_uses_edit_template(self):
        casaEstudiantil = self.casaEstudiantil
        response = self.client.get(f'/casaestudiantil/editar/{casaEstudiantil.id}/')
        self.assertTemplateUsed(response, 'casaestudiantil/casaestudiantil_form.html')

     
    def test_displays_actualizar_casa_estudiantil_form(self):
        casaEstudiantil = self.casaEstudiantil
        response = self.client.get(f'/casaestudiantil/editar/{casaEstudiantil.id}/')
        self.assertIsInstance(response.context['form_casa_estudiantil'], CasaEstudiantilForm)
        self.assertIsInstance(response.context['form_descripcion_casa'], DescripcionCasaForm)
        self.assertIsInstance(response.context['form_telefono'], TelefonoForm)
        self.assertIsInstance(response.context['form_domicilio'], DomicilioForm)
        self.assertContains(response, 'name="nombre"')
        self.assertContains(response, 'name="nombre_dueno"')
        self.assertContains(response, 'name="capacidad"')
        self.assertContains(response, 'name="camas"')
        self.assertContains(response, 'name="cuartos"')
        self.assertContains(response, 'name="sillas"')
        self.assertContains(response, 'name="cocinas"')
        self.assertContains(response, 'name="banios"')
        self.assertContains(response, 'name="numero"')
        self.assertContains(response, 'name="calle"')
        self.assertContains(response, 'name="colonia"')
        self.assertContains(response, 'name="codigo_postal"')
        self.assertContains(response, 'name="estado"')
        self.assertContains(response, 'name="municipio"')
        self.assertContains(response, 'name="telefono"')
    
    def test_delete_only_for_that_casa_estudiantil(self):
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
                nombre = 'Terminal 1',
                telefono_fk = telefono,
                domicilio_fk = domicilio,
                descripcion_casa_fk = descripcionCasa
            )
        correct_casa = self.casaEstudiantil
        other_casa = casaEstudiantil2
        response = self.client.get(f'/casaestudiantil/editar/{correct_casa.id}/')
        self.assertContains(response, 'Frida Kahlo')
        self.assertNotContains(response, 'Terminal 1')

class DeleteCasaEstudiantilTest(TestCase):

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
                nombre = 'Frida Kahlo',
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                descripcion_casa_fk = self.descripcionCasa
            )

    def test_uses_delete_template(self):
        casaEstudiantil = self.casaEstudiantil
        response = self.client.get(f'/casaestudiantil/eliminar/{casaEstudiantil.id}/')
        self.assertTemplateUsed(response, 'casaestudiantil/casaestudiantil_delete.html')
     
    def test_displays_delete_casa_estudiantil_form(self):
        casaEstudiantil = self.casaEstudiantil
        response = self.client.get(f'/casaestudiantil/eliminar/{casaEstudiantil.id}/')
        self.assertContains(response, 'name="author"')

    def test_delete_only_for_that_casa_estudiantil(self):
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
                nombre = 'Terminal 1',
                telefono_fk = telefono,
                domicilio_fk = domicilio,
                descripcion_casa_fk = descripcionCasa
            )
        correct_casa = self.casaEstudiantil
        other_casa = casaEstudiantil2
        response = self.client.get(f'/casaestudiantil/eliminar/{correct_casa.id}/')
        self.assertContains(response, 'Frida Kahlo')
        self.assertNotContains(response, 'Terminal 1')

class URLsTest(TestCase):

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
                nombre = 'Frida Kahlo',
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                descripcion_casa_fk = self.descripcionCasa
            )

    def test_root_url_resolves_to_login_function(self):
        # Verfica si existe la url de inicio sesion
        response = self.client.get('/',)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Inicio Sesión')

    def test_root_url_resolves_to_casa_estudiantil_nuevo_function(self):
        # Verfica si existe la url de casaestudiantil/nuevo
        response = self.client.get('/casaestudiantil/nuevo')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Formulario Casa Estudiantil')

    def test_root_url_resolves_to_mostrar_casa_estudiantil_function(self):
        # Verfica si existe la url de casaestudiantil/mostrar
        response = self.client.get('/casaestudiantil/mostrar')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Listado Casas Estudiantiles')

    def test_root_url_resolves_to_casa_estudiantil_editar_function(self):
        # Verfica si existe la url de casaestudiantil/editar
        response = self.client.get(f'/casaestudiantil/editar/{self.casaEstudiantil.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Formulario Casa Estudiantil')

    def test_root_url_resolves_to_casa_estudiantil_eliminar_function(self):
        # Verfica si existe la url de casaestudiantil/eliminar
        response = self.client.get(f'/casaestudiantil/eliminar/{self.casaEstudiantil.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Elimiar Casa Estudiantil')