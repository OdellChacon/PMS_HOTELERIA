from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarEmpleado/', views.registrarEmpleado),
    path('vistaEmpleado/', views.vistaEmpleado, name='vistaEmpleados'),
    path('edicionEmpleado/<codigo>', views.edicionEmpleado),
    path('editarEmpleado/', views.editarEmpleado),
    path('eliminarEmpleado/<codigo>', views.eliminarEmpleado)
]
