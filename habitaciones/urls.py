from django.urls import path
from . import views


urlpatterns = [
      path('homeh/', views.homeh, name='homeh'),
      path('registrarCategoria/', views.registrarCategoria, name='registrarCategoria'),
      path('quitar_categoria/<id>', views.quitar_categoria, name='quitar_categoria'),
      path('restaurarc/<id>', views.restaurarc, name='restaurarc'),
      path('eliminarc/<id>', views.eliminarc, name='eliminarc'),
      path('restaurarh/<id_num_habitaciones>', views.restaurarh, name='restaurarh'),
      path('eliminarh/<id_num_habitaciones>', views.eliminarh, name='eliminarh'),
      path('papelerac/', views.papelerac, name='papelerac'),
      path('papelerah/', views.papelerah, name='papelerah'),
      path('vistaHabi/', views.vistaHabi, name='vistaHabi'),
      path('asignarh/', views.asignarh, name='asignarh'),
      path('quitar_h/<id_num_habitaciones>', views.quitar_h, name='quitar_h'),
    
]
