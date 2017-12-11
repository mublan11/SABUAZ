from django.shortcuts import render, redirect

from .forms import TelefonoForm
from .forms import DomicilioForm
from .forms import ComedorForm

from .models import Comedor
from apps.solicitante.models import Telefono
from apps.solicitante.models import Domicilio


def create_comedor(request):
    if request.method == 'POST':
        form_comedor= ComedorForm(request.POST, prefix='comedor')
        form_domicilio = DomicilioForm(request.POST, prefix='domicilio')
        form_telefono = TelefonoForm(request.POST, prefix='telefono')
        if form_comedor.is_valid() and form_domicilio.is_valid() \
                and form_telefono.is_valid():
            domicilio = form_domicilio.save()
            telefono = form_telefono.save()
            comedor = form_comedor.save(commit=False)

            comedor.domicilio_fk = domicilio
            comedor.telefono_fk = telefono
            comedor.save()
            return redirect('comedor:comedor_mostrar')
        else:
            print('Fallo la ejecucion')
    else:
        form_comedor = ComedorForm(prefix='comedor')
        form_domicilio = DomicilioForm(prefix='domicilio')
        form_telefono = TelefonoForm(prefix='telefono')
    return render(
        request,
        'comedor/comedor_form.html',
        {
            'form_comedor': form_comedor,
            'form_domicilio': form_domicilio,
            'form_telefono': form_telefono,
        })


def read_comedor(request):
    comedor = Comedor.objects.all()
    context = {'comedor':comedor}
    return render(request, 'comedor/comedor_list.html', context)


def update_comedor(request, pk):
    comedor = Comedor.objects.get(id=pk)
    telefono = Telefono.objects.get(id=comedor.telefono_fk.id)
    domicilio = Domicilio.objects.get(id=comedor.domicilio_fk.id)

    if request.method == "GET":
        form_telefono = TelefonoForm(instance=telefono)
        form_domicilio = DomicilioForm(instance=domicilio)
        form_comedor = ComedorForm(instance=comedor)
    else:
        form_telefono = TelefonoForm(request.POST, instance=telefono)
        form_domicilio = DomicilioForm(request.POST, instance=domicilio)
        form_comedor = ComedorForm(request.POST, instance=comedor)

        condition_1 = form_telefono.is_valid() and form_domicilio.is_valid()

        if condition_1 and form_comedor.is_valid():
            form_telefono.save()
            form_domicilio.save()
            form_comedor.save()
        return redirect('comedor:comedor_mostrar')
    return render(
        request,
        'comedor/comedor_form.html',
        {
            'form_comedor': form_comedor,
            'form_telefono': form_telefono,
            'form_domicilio': form_domicilio,
        })


def delete_comedor(request, pk):
    comedor = Comedor.objects.get(id=pk)
    telefono = Telefono.objects.get(id=comedor.telefono_fk.id)
    domicilio = Domicilio.objects.get(id=comedor.domicilio_fk.id)
    if request.method == "POST":
        comedor.delete()
        telefono.delete()
        domicilio.delete()
        return redirect('comedor:comedor_mostrar')
    return render(request, 'comedor/comedor_delete.html', {'comedor': comedor})
