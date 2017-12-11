from django.conf.urls import url
from django.contrib import admin

from .views import CreateSupervisor
from .views import read_supervisor
from .views import update_supervisor
from .views import delete_supervisor
from django.contrib.auth.views import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^nuevo$',
        CreateSupervisor.as_view(),
        name='supervisor_nuevo'
    ),
    url(
        r'^mostrar$',
        read_supervisor,
        name='supervisor_mostrar'
    ),
    url(
        r'^editar/(?P<pk>\d+)/$',
        update_supervisor,
        name='supervisor_editar'
    ),
    url(
        r'^eliminar/(?P<pk>\d+)/$',
        delete_supervisor,
        name='supervisor_eliminar'
    ),
]
