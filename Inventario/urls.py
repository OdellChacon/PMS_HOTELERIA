from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario),
    path('ingredientes/', views.ingredientes, name="Stock"),
    path('regIngredientes/', views.regIngredientes, name="registrarIngredientes"),
    path('modificarIngrediente/<id>/', views.modIngredientes, name="modificar"),
    path('eliminarIngrediente/<id>/',
         views.dltIngredientes, name="eliminarIngrediente"),
    path('limpieza/', views.limpieza, name="limpieza"),
    path('agregarLimpieza/', views.agregarLimpieza, name="addLimpieza"),
    path('actualizarLimpieza/<id>/', views.actLimpieza, name="modificarLimp"),
    path('eliminarLimpieza/<id>/', views.dltLimpieza, name="eliminarLimp"),
    path('habitaciones/', views.habitaciones, name="habitaciones"),
    path('addHabitacion/', views.addHabitaciones, name="addhabitacion"),
    path('updtHabitacion/<id>/', views.updtHabitaciones, name='actHab'),
    path('deleteHabitacion/<id>/', views.dropHab, name="drophab"),
    path('proveedores/', views.proveedores, name="proveedores"),
    path('addProveedor/', views.addProveedor, name="addProv"),
    path('updateProveedor/<id>/', views.uptProveedor, name="actProveedor"),
    path('deleteProveedor/<id>/', views.dropProveedor, name="eliminarProveedor")
]
