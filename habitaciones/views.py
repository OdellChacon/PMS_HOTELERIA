from django.shortcuts import render, redirect
from .models import categorias
from .models import habitaciones
# Create your views here.


def homeh(request):
    cat = categorias.objects.filter(estatus_categ=1)
    return render(request, "habitaciones1.html", {
        'cat': cat
    })


def registrarCategoria(request):
    guardar_c = categorias(
        nombre_c=request.POST['nombre_c'],
        categoria=request.POST['categoria'],
        precioxdia=request.POST['precioxdia'],
        can_pers=request.POST['can_pers'],
        estatus_categ=1,
    )
    guardar_c.save()
    return redirect('homeh')

# eliminacion logica de categorias


def quitar_categoria(request, id):
    categoria = categorias.objects.get(id=id)
    categoria.estatus_categ = 0
    categoria.save()

    return redirect('homeh')

# restaurar categorias


# asignar habitacion
def vistaHabi(request):
    h = categorias.objects.filter(estatus_categ=1)
    ha1 = habitaciones.objects.filter(
        estatus_habi=1, disponible=False).count()  # disponibles
    ha2 = habitaciones.objects.filter(
        estatus_habi=2, disponible=False).count()  # ocupadas/mantenimiento
    ha3 = habitaciones.objects.filter(
        estatus_habi=3, disponible=False).count()  # reservadas
    h = categorias.objects.filter(estatus_categ=1)
    a1 = habitaciones.objects.filter(
        estatus_habi=1, disponible=False)  # disponibles
    a2 = habitaciones.objects.filter(
        estatus_habi=2, disponible=False)  # ocupadas/mantenimiento
    a3 = habitaciones.objects.filter(
        estatus_habi=3, disponible=False)  # reservadas
    return render(request, "asignar_habi.html", {'h': h, 'ha1': ha1, 'ha2': ha2, 'ha3': ha3, 'a1': a1, 'a2': a2, 'a3': a3})


def asignarh(request):
    categoria = request.POST['categoria']
    id_c = categorias.objects.get(id=categoria)
    guardar_h = habitaciones(

        id_categoria=id_c,
        numero_habitacion=request.POST['nhabi'],
        estatus_habi=request.POST['estatus'],

    )
    guardar_h.save()
    return redirect('vistaHabi')
# eliminacion logica de habitacion


def quitar_h(request, id_num_habitaciones):
    habitacion = habitaciones.objects.get(
        id_num_habitaciones=id_num_habitaciones)
    habitacion.disponible = True
    habitacion.save()

    return redirect('vistaHabi')

# restauracion de categorias mediante papelera de reciclaje


def papelerac(request):
    papelerac = categorias.objects.filter(estatus_categ=0)
    return render(request, "papelerac.html", {'papelerac': papelerac})


def papelerah(request):
    papelerah = habitaciones.objects.filter(disponible=True)
    return render(request, "papelerah.html", {'papelerah': papelerah})
# restauracion de categoria


def restaurarc(request, id):
    categoria = categorias.objects.get(id=id)
    categoria.estatus_categ = 1
    categoria.save()

    return redirect('papelerac')
# eliminar categoria


def eliminarc(request, id):
    categoria = categorias.objects.get(id=id)
    categoria.delete()

    return redirect('papelerac')


# restauracion de habitacion
def restaurarh(request, id_num_habitaciones):
    habitacion = habitaciones.objects.get(
        id_num_habitaciones=id_num_habitaciones)
    habitacion.disponible = False
    habitacion.save()

    return redirect('papelerah')
# eliminar categoria


def eliminarh(request, id_num_habitaciones):
    habitacion = habitaciones.objects.get(
        id_num_habitaciones=id_num_habitaciones)
    habitacion.delete()

    return redirect('papelerah')
