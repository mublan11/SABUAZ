from django.test import TestCase
from apps.solicitante.models import *
from apps.casaestudiantil.forms import *

class AllFormsTest(TestCase):
    # Se crea una Casa Estudiantil
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
                nombre = 'Frida Kahlo',
                telefono_fk = self.telefono,
                domicilio_fk = self.domicilio,
                descripcion_casa_fk = self.descripcionCasa
            )

    def test_form_casa_estudiantil_input_has_css_classes(self):
        form = CasaEstudiantilForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_actualizar_casa_estudiantil_input_has_css_classes(self):
        form = CasaEstudiantilForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_descripcion_casa_input_has_css_classes(self):
        form = DescripcionCasaForm()
        self.assertIn('class="form-control"', form.as_p())
    
    def test_form_telefono_input_has_css_classes(self):
        form = TelefonoForm()
        self.assertIn('class="form-control"', form.as_p())
        
    def test_form_domicilio_input_has_css_classes(self):
        form = DomicilioForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_blank_items_casa_estudiantil_form(self):
        form = CasaEstudiantilForm(data={'nombre': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nombre'], ['This field is required.'])

    def test_form_validation_for_blank_items_telefono_form(self):
        form = TelefonoForm(data={'telefono': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['telefono'], ['This field is required.'])

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

    def test_form_validation_for_blank_items_descripcion_casa_form(self):
        form = DescripcionCasaForm(data={'nombre_dueno': '', 'capacidad': '',
            'camas': '','cuartos': '','sillas': '', 'cocinas': '', 'banios': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nombre_dueno'], ['This field is required.'])
        self.assertEqual(form.errors['capacidad'], ['This field is required.'])
        self.assertEqual(form.errors['camas'], ['This field is required.'])
        self.assertEqual(form.errors['cuartos'], ['This field is required.'])
        self.assertEqual(form.errors['sillas'], ['This field is required.'])
        self.assertEqual(form.errors['cocinas'], ['This field is required.'])
        self.assertEqual(form.errors['banios'], ['This field is required.'])

    # colocar unique al nombre de comedor pablito
    # def test_form_validation_for_duplicate_casas(self):
    #     casaEstudiantil = self.casaEstudiantil
    #     form = CasaEstudiantilForm(data={'nombre': 'Frida Kahlo'})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['id'], ['Casa Estudiantil with this Nombre already exists.'])

    def test_form_save_handles_saving_to_a_casa_estudiantil(self):
        casaEstudiantil = self.casaEstudiantil
        form = CasaEstudiantilForm(data={'nombre': 'Frida Kahlo'})
        casaEstudiantil.save()
        self.assertEqual(casaEstudiantil, CasaEstudiantil.objects.first())
        self.assertEqual(casaEstudiantil.nombre, 'Frida Kahlo')

    def test_form_save(self):
        casaEstudiantil = self.casaEstudiantil
        form = CasaEstudiantilForm(data={'nombre': 'Frida Kahlo'})
        nuevo_casa = casaEstudiantil
        self.assertEqual(nuevo_casa, CasaEstudiantil.objects.all()[0])