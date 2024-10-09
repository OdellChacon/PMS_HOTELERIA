from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteFrm
from django.contrib import messages

# Create your views here.


def Clientes(request):

    osvell = Cliente.objects.all()

    return render(request, "Huespedes.html", {
        'clientes': osvell
    })


def regCliente(request):

    data = {
        'clientes': ClienteFrm()
    }

    if (request.method == "POST"):
        osvell = ClienteFrm(data=request.POST)
        if osvell.is_valid():
            osvell.save()
            messages.success(request, "Cliente Registrado con Exito")
            return redirect("Cliente")

    return render(request, "newCliente.html", data)


def updtCliente(request, id):
    frm = get_object_or_404(Cliente, id=id)

    data = {
        'clientes': ClienteFrm(instance=frm)
    }

    if (request.method == "POST"):
        Jorge = ClienteFrm(data=request.POST, instance=frm)
        if Jorge.is_valid():
            Jorge.save()
            messages.success(request, "Cliente Actualizado Con Exito")
            return redirect("Cliente")

    return render(request, "updateCliente.html", data)


def eliminarCliente(request, id):

    Odra = get_object_or_404(Cliente, id=id)
    Odra.delete()
    messages.success(request, "Cliente Eliminado Con Exito")
    return redirect("Cliente")
