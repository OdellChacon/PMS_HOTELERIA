"""PMS_Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('registro/', views.registro),
    path('dashboard/', include('AdminHome.urls')),
    path('Eventos/', include('Eventos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inventario/', include('Inventario.urls')),
    path('empleados/', include('crud_empleados.urls')),
    path('huespedes/', include('Clientes.urls')),
    path('sugerencias/', include('Sugerencias.urls')),
    path('restaurante/', include('Restaurante.urls')),
    path('carro/', include('carro.urls')),
    path('habitaciones/', include('habitaciones.urls')),
    path('reservas/', include('reservas.urls')),
    path('cerrar_sesion/', views.cerrar_sesion)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
