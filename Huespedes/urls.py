from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarHuesped/', views.registrarHuesped),
    path('vistaHuespedes/', views.vistaHuespedes, name='/vistaHuespedes'),
    path('edicionHuesped/<codigo>', views.edicionHuespedes),
    path('editarHuesped/', views.editarHuesped),
    path('eliminarHuesped/<codigo>', views.eliminarHuespedes)
]
