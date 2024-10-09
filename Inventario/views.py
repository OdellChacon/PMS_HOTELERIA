from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock, Proveedores, artLimpieza, artHabitaciones
from .forms import IngredientesFrm, LimpiezaFrm, HabitacionesFrm, ProveedorFrm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def inventario(request):
    stocks = Stock.objects.all()
    proveedor = Proveedores.objects.all()
    limpieza = artLimpieza.objects.all()
    habitacion = artHabitaciones.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(stocks, 2)
        stocks = paginator.page(page)
    except:
        raise Http404

    try:
        paginator = Paginator(limpieza, 2)
        limpieza = paginator.page(page)
    except:
        raise Http404

    try:
        paginator = Paginator(habitacion, 2)
        habitacion = paginator.page(page)
    except:
        raise Http404

    try:
        paginator = Paginator(proveedor, 2)
        proveedor = paginator.page(page)
    except:
        raise Http404

    return render(request, "inventario.html", {
        'ingredientes': stocks,
        'proveedor': proveedor,
        'art': limpieza,
        'room': habitacion,
        'paginator': paginator
    })


@login_required
def ingredientes(request):

    stocks = Stock.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(stocks, 5)
        stocks = paginator.page(page)
    except:
        raise Http404

    return render(request, "ingredientes.html", {
        'entity': stocks,
        'paginator': paginator
    })


@login_required
def regIngredientes(request):

    data = {
        'ingredientes': IngredientesFrm()
    }

    if (request.method == "POST"):  # Create
        osvell = IngredientesFrm(data=request.POST)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Producto Agregado Con Exito")
            return redirect('Stock')
        else:
            data['mensaje'] = osvell

    return render(request, "regIngredientes.html", data)


@login_required
def modIngredientes(request, id):  # Update
    producto = get_object_or_404(Stock, id=id)

    data = {
        'ingredientes': IngredientesFrm(instance=producto)
    }

    if (request.method == "POST"):
        Osvell = IngredientesFrm(request.POST, instance=producto)
        if Osvell.is_valid():
            Osvell.save()
            messages.success(request, "Producto Actualizado Correctamente")
            return redirect("Stock")
        else:
            data["mensaje"] = "Error al Actualizar"

    return render(request, "actIngredientes.html", data)


@login_required
def dltIngredientes(request, id):
    producto = get_object_or_404(Stock, id=id)
    producto.delete()
    messages.error(request, "Producto Eliminado Correctamente")
    return redirect("Stock")


@login_required
def habitaciones(request):
    habitacion = artHabitaciones.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(habitacion, 5)
        habitacion = paginator.page(page)
    except:
        raise Http404

    return render(request, "habitaciones.html", {
        'entity': habitacion,
        'paginator': paginator
    })


@login_required
def addHabitaciones(request):

    data = {
        'habitaciones': HabitacionesFrm()
    }

    if (request.method == "POST"):
        form = HabitacionesFrm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Agregado con Exito")
            return redirect('habitaciones')

    return render(request, "regHabitaciones.html", data)


@login_required
def updtHabitaciones(request, id):

    hab = get_object_or_404(artHabitaciones, id=id)

    data = {
        'habitaciones': HabitacionesFrm(instance=hab)
    }

    if (request.method == "POST"):
        osvell = HabitacionesFrm(data=request.POST, instance=hab)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Item Actualizado Con Exito")
            return redirect("habitaciones")

    return render(request, 'actHabitaciones.html', data)


@login_required
def dropHab(request, id):
    hab = get_object_or_404(artHabitaciones, id=id)
    hab.delete()
    messages.error(request, "Item Eliminado Con Exito")
    return redirect('habitaciones')


@login_required
def limpieza(request):
    limpieza = artLimpieza.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(limpieza, 5)
        limpieza = paginator.page(page)
    except:
        raise Http404

    return render(request, "art_limpieza.html", {
        'entity': limpieza,
        'paginator': paginator
    })


@login_required
def agregarLimpieza(request):  # Create

    data = {
        'formLimpieza': LimpiezaFrm()
    }

    if (request.method == "POST"):
        osvell = LimpiezaFrm(data=request.POST)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Articulo Agregado Con Exito")
            return redirect("limpieza")

    return render(request, "regLimpieza.html", data)


@login_required
def actLimpieza(request, id):

    art = get_object_or_404(artLimpieza, id=id)

    data = {
        'formLimpieza': LimpiezaFrm(instance=art)
    }

    if (request.method == "POST"):
        osvell = LimpiezaFrm(request.POST, instance=art)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Articulo Actualizado Con Exito")
            return redirect("limpieza")
        else:
            data["mensaje"] = "Error: No se pudo conectar al servidor"

    return render(request, "actLimpieza.html", data)


@login_required
def dltLimpieza(request, id):
    osvell = get_object_or_404(artLimpieza, id=id)
    osvell.delete()
    messages.success(request, "Articulo Eliminado Con Exito")
    return redirect('limpieza')


@login_required
def proveedores(request):
    proveedor = Proveedores.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(proveedor, 5)
        proveedor = paginator.page(page)
    except:
        raise Http404

    return render(request, "proveedores.html", {
        'entity': proveedor,
        'paginator': paginator
    })


@login_required
def addProveedor(request):

    data = {
        'proveedor': ProveedorFrm()
    }

    if (request.method == "POST"):
        osvell = ProveedorFrm(data=request.POST)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Proveedor Agregado Con Exito")
            return redirect('proveedores')

    return render(request, "regProveedor.html", data)


@login_required
def uptProveedor(request, id):

    frm = get_object_or_404(Proveedores, id=id)

    data = {
        'proveedores': ProveedorFrm(instance=frm)
    }

    if (request.method == "POST"):
        osvell = ProveedorFrm(data=request.POST, instance=frm)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Proveedor Actualizado Con Exito")
            return redirect("proveedores")

    return render(request, "actProveedor.html", data)


@login_required
def dropProveedor(request, id):
    frm = get_object_or_404(Proveedores, id=id)
    frm.delete()
    messages.success(request, "Proveedor Eliminado Con Exito")
    return redirect("proveedores")
