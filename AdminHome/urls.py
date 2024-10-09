from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('reportes/', views.reporte),
    path('reportes/charts', views.get_chartView, name='get_chart'),
    path('reportes/chart_stock', views.chart_stock, name='json_chart'),
    path('reportes/chart_habitaciones',
         views.chart_habitaciones, name='json_chart'),
    path('reportes/chart_limpieza', views.chart_limpieza, name='json_chart'),
    path('reportes/cliente', views.reporte_cliente.as_view(),
         name='reportes_cliente'),
    path('reportes/huesped', views.reporte_huesped.as_view(),
         name='reportes_huesped'),
    path('reportes/inventario', views.reporte_inventario.as_view(),
         name='reportes_inventario'),
    path('reportes/sugerencia', views.reporte_sugerencia.as_view(),
         name='reportes_sugerencia'),
    path('reportes/empleados', views.reporte_empleado.as_view(), name='reportes'),
    path('reportes/reservas', views.reporte_reserva.as_view(), name='reportes'),
    path('inventario/', include('Inventario.urls')),
]
