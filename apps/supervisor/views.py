from django.shortcuts import render, redirect

from .forms import SupervisorForm
from .models import Supervisor

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse_lazy


class CreateSupervisor(CreateView):
    model = Supervisor
    form_class = SupervisorForm
    template_name = 'supervisor/supervisor_form.html'
    success_url = reverse_lazy('supervisor:supervisor_mostrar')


def read_supervisor(request):
    supervisor = Supervisor.objects.all()
    context = {'supervisor': supervisor}
    return render(
        request,
        'supervisor/supervisor_list.html',
        context
    )


def update_supervisor(request, pk):
    supervisor = Supervisor.objects.get(id=pk)
    if request.method == "GET":
        form = SupervisorForm(instance=supervisor)
    else:
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
        return redirect('supervisor:supervisor_mostrar')
    return  render(
        request,
        'supervisor/supervisor_form.html',
        {'form':form}
    )


def delete_supervisor(request, pk):
    supervisor = Supervisor.objects.get(id=pk)
    if request.method == "POST":
        supervisor.delete()
        return redirect('supervisor:supervisor_mostrar')
    return render(
        request,
        'supervisor/supervisor_delete.html',
        {'supervisor':supervisor}
    )