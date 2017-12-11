from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login_required

from .views import create_casaestudiantil
from .views import read_casaestudiantil
from .views import update_casaestudiantil
from .views import delete_casaestudiantil


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^nuevo$', create_casaestudiantil,
        name='casaestudiantil_nuevo'
    ),
    url(
        r'^mostrar$',
        read_casaestudiantil,
        name='casaestudiantil_mostrar'
    ),
    url(
        r'^editar/(?P<pk>\d+)/$',
        update_casaestudiantil,
        name='casaestudiantil_editar'
    ),
    url(
        r'^eliminar/(?P<pk>\d+)/$',
        delete_casaestudiantil,
        name='casaestudiantil_eliminar'
    ),
]