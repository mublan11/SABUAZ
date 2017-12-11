from django import forms

from apps.solicitante.models import Solicitante
from apps.solicitante.models import DatosAcademicos
from apps.solicitante.models import Telefono
from apps.solicitante.models import Domicilio
from apps.solicitante.models import Documentos


class SolicitanteForm(forms.ModelForm):

    class Meta:
        model = Solicitante
        fields = (
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'sexo',
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }


class ActualizarSolicitanteForm(forms.ModelForm):

    class Meta:
        model = Solicitante
        fields = (
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'sexo',
            'status',
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class DatosAcademicosForm(forms.ModelForm):
    class Meta:
        model = DatosAcademicos
        fields = (
            'matricula',
            'promedio',
            'unidad_academica',
            'programa_academico',
        )
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'promedio': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_academica': forms.Select(attrs={'class': 'form-control'}),
            'programa_academico': forms.Select(attrs={'class': 'form-control'}),
        }


class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = (
            'telefono',
            'tipo',
        )
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }


class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = (
            'numero',
            'calle',
            'colonia',
            'codigo_postal',
            'estado',
            'municipio',
        )
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
        }


class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = (
            'tipo_beca',
            'tipo_solicitud',
            'estudio_socioeconomico',
            'comprobante_ingresos',
            'ine_padres',
            'boleta_calificaciones',
            'comprobante_inscripcion',
            'carta_compromiso_padres',
            'comprobante_solicitud_linea',
        )
        widgets = {
            'tipo_beca': forms.Select(attrs={'class':'form-control'}),
            'tipo_solicitud': forms.Select(attrs={'class':'form-control'}),
            'estudio_socioeconomico': forms.FileInput(attrs={'class': 'form-control'}),
            'comprobante_ingresos': forms.FileInput(attrs={'class': 'form-control'}),
            'ine_padres': forms.FileInput(attrs={'class': 'form-control'}),
            'comprobante_inscripcion': forms.FileInput(attrs={'class': 'form-control'}),
            'boleta_calificaciones': forms.FileInput(attrs={'class': 'form-control'}),
            'carta_compromiso_padres': forms.FileInput(attrs={'class': 'form-control'}),
            'comprobante_solicitud_linea': forms.FileInput(attrs={'class': 'form-control'}),
        }
