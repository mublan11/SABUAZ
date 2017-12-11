from django import forms

from .models import Supervisor


class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = (
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'comedor_fk',
            'casas_estudiantil_fk',
        )

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(
                attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(
                attrs={'class': 'form-control'}),
            'comedor_fk': forms.Select(
                attrs={'class': 'form-control'}),
            'casas_estudiantil_fk': forms.Select(
                attrs={'class': 'form-control'}),
        }
