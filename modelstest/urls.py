"""modelstest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    url(
        r'^admin/',
        admin.site.urls
    ),
    url(
        r'^solicitante/',
        include(
            'apps.solicitante.urls',
            namespace="solicitante"
        )
    ),
    url(
        r'^comedor/',
        include(
            'apps.comedor.urls',
            namespace="comedor"
        )
    ),
    url(
        r'^casaestudiantil/',
        include(
            'apps.casaestudiantil.urls',
            namespace="casaestudiantil"
        )
    ),
    url(
        r'^supervisor/',
        include(
            'apps.supervisor.urls',
            namespace="supervisor"
        )
    ),
    url(
        r'^usuario/',
        include(
            'apps.usuario.urls',
            namespace="usuario"
        )
    ),
    url(
        r'^accounts/login/',
        login,
        {'template_name': 'index.html'},
        name='login'
    ),
    url(
        r'^$',
        login,
        {'template_name':'index.html'},
        name='login'),
    url(
        r'^logout/',
        logout_then_login,
        name='logout'
    ),
    url(
        r'^servicios/',
        include(
            'apps.serviciosexternos.urls',
            namespace="servicios"
        )
    ),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
