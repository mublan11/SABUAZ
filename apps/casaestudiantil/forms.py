from django import forms

from apps.solicitante.models import Telefono
from apps.solicitante.models import Domicilio

from .models import CasaEstudiantil
from .models import DescripcionCasa


class CasaEstudiantilForm(forms.ModelForm):
    class Meta:
        model = CasaEstudiantil
        fields = (
            'nombre',
        )
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = (
            'telefono',
        )
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
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


class DescripcionCasaForm (forms.ModelForm):
    class Meta:
        model = DescripcionCasa
        fields = (
            'nombre_dueno',
            'capacidad',
            'camas',
            'cuartos',
            'sillas',
            'cocinas',
            'banios',
        )
        widgets = {
            'nombre_dueno': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.TextInput(attrs={'class': 'form-control'}),
            'camas': forms.TextInput(attrs={'class': 'form-control'}),
            'cuartos': forms.TextInput(attrs={'class': 'form-control'}),
            'sillas': forms.TextInput(attrs={'class': 'form-control'}),
            'cocinas': forms.TextInput(attrs={'class': 'form-control'}),
            'banios': forms.TextInput(attrs={'class': 'form-control'}),
        }