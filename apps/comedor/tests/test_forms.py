from django.test import TestCase
from apps.solicitante.models import *
from apps.comedor.forms import *
#8 , 9 si descomentamos la otra
class AllFormsTest(TestCase):
    # Se crea un comedor
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
            nombre = "Psicología", 
            telefono_fk = self.telefono,
            domicilio_fk = self.domicilio
            )

    def test_form_comedor_input_has_css_classes(self):
        form = ComedorForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_actualizar_comedor_input_has_css_classes(self):
        form = ComedorForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_telefono_input_has_css_classes(self):
        form = TelefonoForm()
        self.assertIn('class="form-control"', form.as_p())
        
    def test_form_domicilio_input_has_css_classes(self):
        form = DomicilioForm()
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_blank_items_comedor_form(self):
        form = ComedorForm(data={'nombre': ''})
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
    
    # colocar unique al nombre de comedor pablito
    # def test_form_validation_for_duplicate_comedores(self):
    #     comedor = self.comedor
    #     form = ComedorForm(data={'nombre': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['nombre'], ['Datos academicos with this Matricula already exists.'])

    def test_form_save_handles_saving_to_a_comedor(self):
        comedor = self.comedor
        form = ComedorForm(data={'nombre': 'Psicología'})
        comedor.save()
        self.assertEqual(comedor, Comedor.objects.first())
        self.assertEqual(comedor.nombre, 'Psicología')

    def test_form_save(self):
        comedor = self.comedor
        form = ComedorForm(data={'nombre': 'Psicología'})
        nuevo_comedor = comedor
        self.assertEqual(nuevo_comedor, Comedor.objects.all()[0])