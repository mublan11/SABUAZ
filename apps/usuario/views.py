from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from apps.usuario.forms import RegistroForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('solicitante:solicitante_mostrar')
