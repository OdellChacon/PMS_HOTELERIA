from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from urllib import request
from datetime import datetime, date, time, timedelta
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from .models import datos_reserva, habitaciones, categorias, metodos_pagos, reservaciones
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# vista de cargar datos de reserva


def vista1(request):
    cat = categorias.objects.filter(estatus_categ=1)
    return render(request, 'reservas/vista_1.html', {"cat": cat})
# vista de reserva


@login_required
def vista2(request):
    habi = habitaciones.objects.filter(disponible=False)

    return render(request, 'reservas/vista_2.html', {"habi": habi})


def vista3(request):
    dias = datos_reserva.objects.latest('dias_pago')
    id_dr = datos_reserva.objects.latest('id')
    filtro_categoria = datos_reserva.objects.latest('id')

    habi1 = habitaciones.objects.filter(estatus_habi=1)
    m_pago = metodos_pagos.objects.all()

    return render(request, 'reservas/vista_3.html', {"cate": filtro_categoria, "dias": dias, "id_dr": id_dr, "habi1": habi1, "m_pago": m_pago})


def vista4(request):
    id_r = reservaciones.objects.latest('id')
    rese1 = datos_reserva.objects.latest('id')
    return render(request, 'reservas/vista_4.html', {"id_r": id_r, "rese1": rese1})

# para ver estado de la reserva


def codigo_reserva(request):
    userid = request.user.id
    num_reservas = reservaciones.objects.filter(
        id_datos_reserva__id_usuario=userid).count()
    reservas = reservaciones.objects.filter(
        id_datos_reserva__id_usuario=userid)
    return render(request, 'reservas/codigo.html', {"reservas": reservas, "numero": num_reservas})


def crear_datos_reserva(request):

    _userid = request.user.id
    cat = request.POST['categoria']
    cat1 = categorias.objects.get(id=cat)

    datos_r = datos_reserva(
        id_usuario=User.objects.get(id=_userid),
        id_categoria=cat1,
        f_entrada=request.POST['timeStart'],
        f_salida=request.POST['timeEnd'],
        num_personas=request.POST['c_personas'],
        num_niños=request.POST['c_ninos'],


        n_ocupante=request.POST['nombre_o'],
        estatus_datos_rese=1,
        dias_pago=request.POST['daysDiscount'],

    )

    datos_r.save()
    return redirect('vista2')


def guardar_reserva(request):
    diasp = request.POST['dias']
    precioxdia = request.POST['precio_c']
    total = int(diasp) * int(precioxdia)
    id_dr = datos_reserva.objects.latest('id')
    id_ = request.POST['habitaciones']
    _pago = request.POST['pago']

    id_ha = habitaciones.objects.get(id_num_habitaciones=id_)
    habitacion = habitaciones.objects.get(id_num_habitaciones=id_)
    habitacion.estatus_habi = 3
    habitacion.save()
    id_pa = metodos_pagos.objects.get(id=_pago)
    reserva = reservaciones(

        id_datos_reserva=id_dr,
        id_num_habitaciones=id_ha,
        nombre_r=request.POST['nombre'],
        apellido_r=request.POST['apellido'],
        telefono=request.POST['telefonor'],
        Forma_pago=id_pa,
        tarifa_pago=total,
        fecha_reserva=datetime.now(),
        hora_de_llegada=request.POST['hora'],
        estatus_reservacion=1,
        peticiones=request.POST['peticionesr'],

    )
    reserva.save()
    return redirect('vista4')


def register(request):
    data = {
        'form': CustomUserCreationForm()

    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(
                username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('vista1')
        data['form'] = user_creation_form
    return render(request, 'registration/register.html', data)

    # Dashboard


def reservas(request):
    res = reservaciones.objects.filter(
        disponible=False).order_by('id_datos_reserva__f_entrada')
    actual = date.today()
    return render(request, 'reservas/verReservas.html', {
        'res': res, 'hoy': actual
    })
# detalles de cada reserva


def detalles(request, id):

    res = reservaciones.objects.get(id=id)
    return render(request, 'reservas/detalles.html', {
        'res': res
    })
    # activar reserva


def activar(request, id):
    reserva = reservaciones.objects.get(id=id)
    reserva.estatus_reservacion = 0
    reserva.save()
    return render(request, 'reservas/activada.html')

# eliminar la reserva de forma logica


def eliminar_reserva(request, id):
    eliminar = reservaciones.objects.get(id=id)
    eliminar.disponible = True
    eliminar.save()

    return redirect('reservas')

  # buscar reserva


def buscar(request):
    cod = request.POST['idr']
    res = reservaciones.objects.get(id=cod)
    return render(request, 'reservas/busqueda.html', {'res': res})

# insertar metodo de pago


def pagos(request):
    pago = metodos_pagos.objects.all()
    return render(request, 'reservas/pagos.html', {'pago': pago})

# agregar


def agregar_p(request):

    agregar_p = metodos_pagos(

        metodo=request.POST['metodo'],
        descripcion=request.POST['descripcion'],


    )

    agregar_p.save()
    return redirect('pagos')
