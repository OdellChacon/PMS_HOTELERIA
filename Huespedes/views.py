from django.shortcuts import render, redirect
from .models import Huesped

# Create your views here.


def home(request):
    return render(request, "gestionHuespedes.html")


def vistaHuespedes(request):
    x = Huesped.objects.all()
    return render(request, "vistaHuespedes.html", {
        'huespedes': x
    })


def registrarHuesped(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    correo = request.POST['txtCorreo']
    direccion = request.POST['txtDireccion']

    huesped = Huesped.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, telefono=telefono, correo=correo, direccion=direccion)

    return redirect('vistaHuespedes.html')


def edicionHuespedes(request, codigo):
    huesped = Huesped.objects.get(codigo=codigo)
    return render(request, "edicionHuesped.html", {"huesped": huesped})


def editarHuesped(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    correo = request.POST['txtCorreo']
    direccion = request.POST['txtDireccion']

    huesped = Huesped.objects.get(codigo=codigo)
    huesped.nombre = nombre
    huesped.apellido = apellido
    huesped.telefono = telefono
    huesped.correo = correo
    huesped.direccion = direccion
    huesped.save()

    return redirect('vistaHuespedes')


def eliminarHuespedes(request, codigo):
    huesped = Huesped.objects.get(codigo=codigo)
    huesped.delete()

    return redirect('vistaHuespedes')
