from django import forms

from apps.solicitante.models import Telefono
from apps.solicitante.models import Domicilio

from .models import Comedor


class ComedorForm(forms.ModelForm):
    class Meta:
        model = Comedor
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