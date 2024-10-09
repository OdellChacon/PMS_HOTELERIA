from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainRestaurante, name="main"),
    path('agregarComida/', views.Comida, name="comida"),
    path('restaurante/', views.Restaurante, name="restaurante"),
    path('uptPlato/<id>/', views.uptPlatillo, name="update"),
    path('dltPlato/<id>/', views.dltPlatillo, name="delete"),
    path('finalizar/', views.finalizar, name="finalizar")
]
