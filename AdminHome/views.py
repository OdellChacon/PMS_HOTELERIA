import logging
import datetime
from random import randrange
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from crud_empleados.models import Empleado
from Inventario.models import artHabitaciones, artLimpieza, Proveedores, Stock
from reservas.models import reservaciones
from Inventario.models import moneda, semana, limpieza, sistemaUnidades, producType
from Clientes.models import Cliente
from Huespedes.models import Huesped
from Sugerencias.models import Sugerencias
from django.views.generic import View
from django.core.paginator import Paginator
from django.http import Http404
from AdminHome.utils import render_to_pdf
# Create your views here.


@login_required
def dashboard(request):

    empleados = Empleado.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(empleados, 6)
        empleados = paginator.page(page)
    except:
        raise Http404

    return render(request, "dashboard.html", {
        'empleado': empleados
    })


def reporte(request):
    return render(request, "reportes/reportes_list.html")


def get_chartView(request):
    return render(request, "reportes/get_chart.html")


def chart_limpieza(request):
    articulos_limpieza = artLimpieza.objects.all()
    articulos = [articulos.Producto for articulos in articulos_limpieza]
    cantidad = [cantidad.Cantidad for cantidad in articulos_limpieza]
    chart = {
        'xAxis': [
            {
                'type': "category",
                'data': articulos
            }
        ],
        'yAxis': [
            {
                'type': "value"
            }
        ],
        'series': [
            {
                'data': cantidad,
                'type': "bar",
            }
        ]
    }
    return JsonResponse(chart)


def chart_stock(request):
    stock = Stock.objects.all()
    stock_products = [stock.Producto for stock in stock]
    stock_cantidad = [stock.Cantidad for stock in stock]

    chart = {
        'xAxis': [
            {
                'type': "category",
                'data': stock_products
            }
        ],
        'yAxis': [
            {
                'type': "value"
            }
        ],
        'series': [
            {
                'data': stock_cantidad,
                'type': "bar",
            }
        ]
    }
    return JsonResponse(chart)


def chart_habitaciones(request):
    articulos_habitaciones = artHabitaciones.objects.all()
    articulos = [articulos.Producto for articulos in articulos_habitaciones]
    cantidad = [cantidad.Cantidad for cantidad in articulos_habitaciones]
    chart = {
        'xAxis': [
            {
                'type': "category",
                'data': articulos
            }
        ],
        'yAxis': [
            {
                'type': "value"
            }
        ],
        'series': [
            {
                'data': cantidad,
                'type': "bar",
            }
        ]
    }
    return JsonResponse(chart)


class reporte_empleado(View):
    def get(self, request, *args, **kwargs):
        template_name = "reportes/reporte_empleados.html"
        empleados = Empleado.objects.all()
        data = {
            'count': empleados.count(),
            'empleados': empleados
        }
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')


class reporte_cliente(View):
    def get(self, request, *args, **kwargs):
        template_name = "reportes/reporte_cliente.html"
        cliente = Cliente.objects.all()
        data = {
            'count': cliente.count(),
            'cliente': cliente
        }
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')


class reporte_reserva(View):
    def get(self, request, *args, **kwargs):
        template_name = "reportes/reporte_reserva.html"
        reserva = reservaciones.objects.all()
        hoy = datetime.datetime.now().date()
        hace_una_semana = hoy - datetime.timedelta(days=7)
        fecha_reserva_array = reserva.values_list('fecha_reserva', flat=True)
        fecha_reserva = list(fecha_reserva_array)
        fechas_filtradas = [
            fecha for fecha in fecha_reserva if hace_una_semana <= fecha <= hoy]

        data = {
            'count': reserva.count(),
            'reserva': reserva,
            'hoy': hoy,
            'hace_una_semana': hace_una_semana,
            'fechas_filtradas': len(fechas_filtradas)
        }
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')


class reporte_sugerencia(View):
    def get(self, request, *args, **kwargs):
        template_name = "reportes/reporte_sugerencia.html"
        sugerencia = Sugerencias.objects.all()
        data = {
            'count': sugerencia.count(),
            'sugerencia': sugerencia
        }
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')


class reporte_huesped(View):
    def get(self, request, *args, **kwargs):
        template_name = "reportes/reporte_huesped.html"
        huesped = Huesped.objects.all()
        data = {
            'count': huesped.count(),
            'huesped': huesped
        }
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')


class reporte_inventario(View):
    def get(self, request, *args, **kwargs):
        template_name = "reportes/reporte_inventario.html"
        proveedores = Proveedores.objects.all()
        art_habitaciones = artHabitaciones.objects.all()
        art_limpieza = artLimpieza.objects.all()
        stock = Stock.objects.all()
        data = {
            'count_proveedores': proveedores.count(),
            'proveedores': proveedores,
            'count_art_hab': art_habitaciones.count(),
            'art_habitaciones': art_habitaciones,
            'count_art_limp': art_limpieza.count(),
            'art_limpieza': art_limpieza,
            'count_stock': stock.count(),
            'stock': stock,
            'moneda': moneda,
            'semana': semana,
            'limpieza': limpieza,
            'unidad': sistemaUnidades,
            'type': producType
        }
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')
