from django.conf.urls import url
from django.contrib import admin

from .views import create_comedor
from .views import read_comedor
from .views import update_comedor
from .views import delete_comedor
from django.contrib.auth.views import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(
        r'^nuevo$',
        create_comedor,
        name='comedor_nuevo'
    ),
    url(
        r'^mostrar$',
        read_comedor,
        name='comedor_mostrar'
    ),
    url(
        r'^editar/(?P<pk>\d+)/$',
        update_comedor,
        name='comedor_editar'
    ),
    url(
        r'^eliminar/(?P<pk>\d+)/$',
        delete_comedor,
        name='comedor_eliminar'
    ),
]