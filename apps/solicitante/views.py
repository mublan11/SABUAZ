from django.shortcuts import render, redirect, get_object_or_404

from .forms import SolicitanteForm
from .forms import DatosAcademicosForm
from .forms import TelefonoForm
from .forms import DomicilioForm
from .forms import DocumentosForm
from .forms import ActualizarSolicitanteForm

from .models import Solicitante
from .models import Domicilio
from .models import Telefono
from .models import DatosAcademicos
from .models import Documentos



def create_solicitante(request):
    if request.method == 'POST':
        form_solicitante = SolicitanteForm(request.POST, prefix='solicitante')
        form_datos_academicos = DatosAcademicosForm(request.POST, prefix='datos_academicos')
        form_telefono = TelefonoForm(request.POST, prefix='telefono')
        form_domicilio = DomicilioForm(request.POST, prefix='domicilio')
        form_documentos = DocumentosForm(request.POST or None, request.FILES or None, prefix='documentos')

        condicion_1 = form_solicitante.is_valid() and form_datos_academicos.is_valid()
        condicion_2 = form_telefono.is_valid() and form_domicilio.is_valid() and form_documentos.is_valid()

        if condicion_1 and condicion_2:
            domicilio = form_domicilio.save()
            telefono = form_telefono.save()
            datos_academicos = form_datos_academicos.save()
            documentos = form_documentos.save()
            solicitante = form_solicitante.save(commit=False)

            solicitante.domicilio_fk = domicilio
            solicitante.telefono_fk = telefono
            solicitante.datos_academicos_fk = datos_academicos
            solicitante.documentos_fk = documentos
            solicitante.save()
            return redirect('solicitante:solicitante_mostrar')
        else:
            print("failed!")
    else:
        form_telefono = TelefonoForm(prefix='telefono')
        form_domicilio = DomicilioForm(prefix='domicilio')
        form_datos_academicos = DatosAcademicosForm(prefix='datos_academicos')
        form_documentos = DocumentosForm(prefix='documentos')
        form_solicitante = SolicitanteForm(prefix='solicitante')

    return render(
        request,
        'solicitante/solicitante_form.html',
        {
            'form_solicitante': form_solicitante,
            'form_datos_academicos': form_datos_academicos,
            'form_telefono': form_telefono,
            'form_domicilio': form_domicilio,
            'form_documentos': form_documentos,
        })


def create_solicitante_solicitante(request):
    if request.method == 'POST':
        form_solicitante = SolicitanteForm(request.POST, prefix='solicitante')
        form_datos_academicos = DatosAcademicosForm(request.POST, prefix='datos_academicos')
        form_telefono = TelefonoForm(request.POST, prefix='telefono')
        form_domicilio = DomicilioForm(request.POST, prefix='domicilio')
        form_documentos = DocumentosForm(request.POST or None, request.FILES or None, prefix='documentos')

        condicion_1 = form_solicitante.is_valid() and form_datos_academicos.is_valid()
        condicion_2 = form_telefono.is_valid() and form_domicilio.is_valid() and form_documentos.is_valid()

        if condicion_1 and condicion_2:
            domicilio = form_domicilio.save()
            telefono = form_telefono.save()
            datos_academicos = form_datos_academicos.save()
            documentos = form_documentos.save()
            solicitante = form_solicitante.save(commit=False)

            solicitante.domicilio_fk = domicilio
            solicitante.telefono_fk = telefono
            solicitante.datos_academicos_fk = datos_academicos
            solicitante.documentos_fk = documentos
            solicitante.save()
            return redirect('usuario:registrar')
        else:
            print("failed!")
    else:
        form_telefono = TelefonoForm(prefix='telefono')
        form_domicilio = DomicilioForm(prefix='domicilio')
        form_datos_academicos = DatosAcademicosForm(prefix='datos_academicos')
        form_documentos = DocumentosForm(prefix='documentos')
        form_solicitante = SolicitanteForm(prefix='solicitante')

    return render(
        request,
        'solicitante/solicitante_form2.html',
        {
            'form_solicitante': form_solicitante,
            'form_datos_academicos': form_datos_academicos,
            'form_telefono': form_telefono,
            'form_domicilio': form_domicilio,
            'form_documentos': form_documentos,
        })


def read_solicitante(request):
    solicitante = Solicitante.objects.all()
    context = {'solicitante':solicitante}
    return render(request, 'solicitante/solicitante_list.html', context)


def update_solicitante(request, pk):
    solicitante = Solicitante.objects.get(id=pk)
    datos_academicos = DatosAcademicos.objects.get(id=solicitante.datos_academicos_fk.id)
    telefono = Telefono.objects.get(id=solicitante.telefono_fk.id)
    domicilio = Domicilio.objects.get(id=solicitante.domicilio_fk.id)
    documentos = Documentos.objects.get(id=solicitante.documentos_fk.id)

    if request.method == "GET":
        form_telefono = TelefonoForm(instance=telefono)
        form_domicilio = DomicilioForm(instance=domicilio)
        form_datos_academicos = DatosAcademicosForm(instance=datos_academicos)
        form_documentos = DocumentosForm(request.POST or None, request.FILES or None, instance=documentos)
        form_solicitante = ActualizarSolicitanteForm(instance=solicitante)
    else:
        form_telefono = TelefonoForm(request.POST, instance=telefono)
        form_domicilio = DomicilioForm(request.POST, instance=domicilio)
        form_datos_academicos = DatosAcademicosForm(request.POST, instance=datos_academicos)
        form_documentos = DocumentosForm(request.POST or None, request.FILES or None, request.POST, instance=documentos)
        form_solicitante = ActualizarSolicitanteForm(request.POST, instance=solicitante)

        condition_1 = form_telefono.is_valid() and form_domicilio.is_valid() and form_datos_academicos.is_valid()
        condition_2 = form_documentos.is_valid() and form_solicitante.is_valid()

        if condition_1 and condition_2:
            form_telefono.save()
            form_domicilio.save()
            form_datos_academicos.save()
            form_documentos.save()
            form_solicitante.save()
        return redirect('solicitante:solicitante_mostrar')
    return render(
        request,
        'solicitante/solicitante_form.html',
        {
            'form_solicitante': form_solicitante,
            'form_datos_academicos': form_datos_academicos,
            'form_telefono': form_telefono,
            'form_domicilio': form_domicilio,
            'form_documentos': form_documentos,
        })


def pendiente(request, pk):
    solicitante = Solicitante.objects.get(id=pk)
    solicitante.status = "PENDIENTE"
    solicitante.save()
    return redirect('solicitante:solicitante_mostrar')


def update_status_solicitante(request, pk):
    solicitante = Solicitante.objects.get(id=pk)
    datos_academicos = DatosAcademicos.objects.get(id=solicitante.datos_academicos_fk.id)
    telefono = Telefono.objects.get(id=solicitante.telefono_fk.id)
    domicilio = Domicilio.objects.get(id=solicitante.domicilio_fk.id)
    documentos = Documentos.objects.get(id=solicitante.documentos_fk.id)

    if request.method == "GET":
        form_telefono = TelefonoForm(instance=telefono)
        form_domicilio = DomicilioForm(instance=domicilio)
        form_datos_academicos = DatosAcademicosForm(instance=datos_academicos)
        form_documentos = DocumentosForm(instance=documentos)
        form_solicitante = ActualizarSolicitanteForm(instance=solicitante)
    else:
        form_telefono = TelefonoForm(request.POST, instance=telefono)
        form_domicilio = DomicilioForm(request.POST, instance=domicilio)
        form_datos_academicos = DatosAcademicosForm(request.POST, instance=datos_academicos)
        form_documentos = DocumentosForm(request.POST, instance=documentos)
        form_solicitante = ActualizarSolicitanteForm(request.POST, instance=solicitante)

        condition_1 = form_telefono.is_valid() and form_domicilio.is_valid() and form_datos_academicos.is_valid()
        condition_2 = form_documentos.is_valid() and form_solicitante.is_valid()

        if condition_1 and condition_2:
            form_telefono.save()
            form_domicilio.save()
            form_datos_academicos.save()
            form_documentos.save()
            form_solicitante.save()
        return redirect('solicitante:solicitante_mostrar')
    return render(
        request,
        'solicitante/solicitante_status.html',
        {
            'form_solicitante': form_solicitante,
        })


def delete_solicitante(request, pk):
    solicitante = Solicitante.objects.get(id=pk)
    datos_academicos = DatosAcademicos.objects.get(id=solicitante.datos_academicos_fk.id)
    telefono = Telefono.objects.get(id=solicitante.telefono_fk.id)
    domicilio = Domicilio.objects.get(id=solicitante.domicilio_fk.id)
    documentos = Documentos.objects.get(id=solicitante.documentos_fk.id)
    if request.method == "POST":
        solicitante.delete()
        datos_academicos.delete()
        telefono.delete()
        domicilio.delete()
        documentos.delete()
        return redirect('solicitante:solicitante_mostrar')
    return render(request, 'solicitante/solicitante_delete.html', {'solicitante': solicitante})


