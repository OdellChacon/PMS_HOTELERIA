from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Clientes, name='Cliente'),
    path('newCliente/', views.regCliente, name="registrarHuesped"),
    path('updateCliente/<id>/', views.updtCliente, name="actualizarCliente"),
    path('eliminarCliente/<id>/', views.eliminarCliente, name="eliminar")
]
