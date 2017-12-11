from django.shortcuts import render
from django.shortcuts import redirect

from .forms import CasaEstudiantilForm
from .forms import DescripcionCasaForm
from .forms import DomicilioForm
from .forms import TelefonoForm

from .models import DescripcionCasa
from .models import CasaEstudiantil

from apps.solicitante.models import Telefono
from apps.solicitante.models import Domicilio


def create_casaestudiantil(request):
    if request.method == 'POST':
        form_casa_estudiantil = CasaEstudiantilForm(request.POST, prefix='casa_estudiantil')
        form_descripcion_casa = DescripcionCasaForm(request.POST, prefix='descripcion_casa')
        form_domicilio = DomicilioForm(request.POST, prefix='domicilio')
        form_telefono = TelefonoForm(request.POST, prefix='telefono')

        condition_1 = form_descripcion_casa.is_valid() and form_casa_estudiantil.is_valid()
        condition_2 = form_domicilio.is_valid() and form_telefono.is_valid()

        if condition_1 and condition_2:
            domicilio = form_domicilio.save()
            telefono = form_telefono.save()
            descripcion_casa = form_descripcion_casa.save()
            casa_estudiantil = form_casa_estudiantil.save(commit=False)

            casa_estudiantil.domicilio_fk = domicilio
            casa_estudiantil.telefono_fk = telefono
            casa_estudiantil.descripcion_casa_fk = descripcion_casa
            casa_estudiantil.save()
            return redirect('casaestudiantil:casaestudiantil_mostrar')
        else:
            print('Fallo la ejecucion')
    else:
        form_casa_estudiantil = CasaEstudiantilForm(prefix='casa_estudiantil')
        form_descripcion_casa = DescripcionCasaForm(prefix='descripcion_casa')
        form_domicilio = DomicilioForm(prefix='domicilio')
        form_telefono = TelefonoForm(prefix='telefono')
    return render(
        request,
        'casaestudiantil/casaestudiantil_form.html',
        {
            'form_casa_estudiantil': form_casa_estudiantil,
            'form_descripcion_casa': form_descripcion_casa,
            'form_domicilio': form_domicilio,
            'form_telefono': form_telefono,
        })


def read_casaestudiantil(request):
    casa_estudiantil = CasaEstudiantil.objects.all()
    context = {'casa_estudiantil': casa_estudiantil}
    return render(request, 'casaestudiantil/casaestudiantil_list.html', context)


def update_casaestudiantil(request, pk):
    casa_estudiantil = CasaEstudiantil.objects.get(id=pk)
    descripcion_casa = DescripcionCasa.objects.get(id=casa_estudiantil.descripcion_casa_fk.id)
    telefono = Telefono.objects.get(id=casa_estudiantil.telefono_fk.id)
    domicilio = Domicilio.objects.get(id=casa_estudiantil.domicilio_fk.id)

    if request.method == "GET":
        form_telefono = TelefonoForm(instance=telefono)
        form_domicilio = DomicilioForm(instance=domicilio)
        form_descripcion_casa = DescripcionCasaForm(instance=descripcion_casa)
        form_casa_estudiantil = CasaEstudiantilForm(instance=casa_estudiantil)

    else:
        form_telefono = TelefonoForm(request.POST, instance=telefono)
        form_domicilio = DomicilioForm(request.POST, instance=domicilio)
        form_descripcion_casa = DescripcionCasaForm(request.POST, instance=descripcion_casa)
        form_casa_estudiantil = CasaEstudiantilForm(request.POST, instance=casa_estudiantil)

        condition_1 = form_casa_estudiantil.is_valid() and form_descripcion_casa.is_valid()
        condition_2 = form_domicilio.is_valid() and form_telefono.is_valid()

        if condition_1 and condition_2:
            form_telefono.save()
            form_domicilio.save()
            form_descripcion_casa.save()
            form_casa_estudiantil.save()
        return redirect('casaestudiantil:casaestudiantil_mostrar')
    return render(
        request,
        'casaestudiantil/casaestudiantil_form.html',
        {
            'form_casa_estudiantil': form_casa_estudiantil,
            'form_descripcion_casa': form_descripcion_casa,
            'form_domicilio': form_domicilio,
            'form_telefono': form_telefono,
        })


def delete_casaestudiantil(request, pk):
    casa_estudiantil = CasaEstudiantil.objects.get(id=pk)
    descripcion_casa = CasaEstudiantil.objects.get(id=casa_estudiantil.descripcion_casa_fk.id)
    telefono = Telefono.objects.get(id=casa_estudiantil.telefono_fk.id)
    domicilio = Domicilio.objects.get(id=casa_estudiantil.domicilio_fk.id)

    if request.method == "POST":
        casa_estudiantil.delete()
        descripcion_casa.delete()
        telefono.delete()
        domicilio.delete()
        return redirect('casaestudiantil:casaestudiantil_mostrar')
    return render(request, 'casaestudiantil/casaestudiantil_delete.html', {'casa_estudiantil': casa_estudiantil})
