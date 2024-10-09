from django.urls import path
from .views import vista1, vista2, vista3, vista4, eliminar_reserva, buscar, pagos, agregar_p
from .views import crear_datos_reserva, register, guardar_reserva, codigo_reserva, reservas, detalles, activar


urlpatterns = [
    path('vista1/', vista1, name='vista1'),
    path('crear_datos_reserva', crear_datos_reserva, name='crear_datos_reserva'),
    path('guardar_reserva/', guardar_reserva, name='guardar_reserva'),
    path('register/', register, name='register'),
    path('vista2/', vista2, name='vista2'),
    path('vista3/', vista3, name='vista3'),
    path('vista4/', vista4, name='vista4'),
    path('codigo_reserva/', codigo_reserva, name='codigo_reserva'),
    path('reservas/', reservas, name='reservas'),
    path('detalles/<id>', detalles, name='detalles'),
    path('activar/<id>', activar, name='activar'),
    path('eliminar_reserva/<id>', eliminar_reserva, name='eliminar_reserva'),
    path('buscar', buscar, name='buscar'),
    path('pagos', pagos, name='pagos'),
    path('agregar_p', agregar_p, name='agregar_p'),
   
]
