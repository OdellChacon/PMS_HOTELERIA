from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoFrm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


@login_required
def mainRestaurante(request):

    platillo = Producto.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(platillo, 5)
        platillo = paginator.page(page)
    except:
        raise Http404

    return render(request, "Main.html", {
        'entity': platillo,
        'paginator': paginator
    })


def Restaurante(request):

    menu = Producto.objects.all()

    return render(request, "Restaurante.html", {
        'menu': menu
    })


@login_required
def Comida(request):

    data = {
        'restaurante': ProductoFrm()
    }

    if (request.method == "POST"):
        osvell = ProductoFrm(data=request.POST, files=request.FILES)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Plato Agregado Con Exito")
            return redirect("main")

    return render(request, "Agregar.html", data)


@login_required
def uptPlatillo(request, id):

    plato = get_object_or_404(Producto, id=id)

    data = {
        'restaurante': ProductoFrm(instance=plato)
    }

    if (request.method == "POST"):
        rest = ProductoFrm(data=request.POST,
                           instance=plato, files=request.FILES)
        if rest.is_valid():
            rest.save()
            messages.success(request, "Plato Actualizado Con Exito")
            return redirect("main")

    return render(request, "Actualizar.html", data)


@login_required
def dltPlatillo(request, id):
    plato = get_object_or_404(Producto, id=id)
    plato.delete()
    messages.success(request, "Plato Eliminado Con Exito")
    return redirect('main')


def finalizar(request):
    return render(request, "Compra.html")
