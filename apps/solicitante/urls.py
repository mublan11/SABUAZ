from django.conf.urls import url
from django.contrib import admin

from .views import create_solicitante
from .views import read_solicitante
from .views import update_solicitante
from .views import delete_solicitante
from .views import create_solicitante_solicitante

from django.contrib.auth.views import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^nuevo$',
        create_solicitante,
        name='solicitante_nuevo'
    ),
    url( # NUEVO SOLICITANTE PERO SIN ACCEDER AL SISTEMA, ESTE LO HACEN LOS SOLICITANTES
        r'^nuevo_solicitante$',
        create_solicitante_solicitante,
        name='solicitante_nuevo_sol'
    ),
    url(
        r'^mostrar$',
        read_solicitante,
        name='solicitante_mostrar'
    ),
    url(
        r'^editar/(?P<pk>\d+)/$',
        update_solicitante,
        name='solicitante_editar'
    ),
    url(
        r'^eliminar/(?P<pk>\d+)/$',
        delete_solicitante,
        name='solicitante_eliminar'
    ),

]
