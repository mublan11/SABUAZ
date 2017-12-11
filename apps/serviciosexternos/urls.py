from django.conf.urls import url
from .views import ListServiciosExternos
from .views import DetailServiciosExternos

urlpatterns = [
    url(
        r'^servicios/$',
        ListServiciosExternos.as_view(),
        name="lista_servicios"),
    url(
        r'^servicio/(?P<pk>[0-9]+)$',
        DetailServiciosExternos.as_view(),
        name="detail_servicio"),
]
