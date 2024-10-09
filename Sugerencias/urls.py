from django.urls import path
from . import views

urlpatterns = [
    path('', views.verSugerencias, name='verSugerencias'),
    path('hacerSugerencia/', views.newSugerencias, name='Sugerencias'),
    path('leerSugerencia/<id>/', views.leerSugerencia, name="leer")
]
