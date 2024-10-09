from django.shortcuts import render, redirect
from .models import Empleado
from .forms import CustomUserCreationForm
# Create your views here.


def home(request):
    return render(request, "gestionEmpleados.html")


def vistaEmpleado(request):
    x = Empleado.objects.all()
    return render(request, "vistaEmpleados.html", {
        'empleados': x
    })


def registrarEmpleado(request):

    data = {
        'empleados': CustomUserCreationForm()
    }

    return render(request, "gestionEmpleados.html", data)


def edicionEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    return render(request, "edicionEmpleados.html", {"empleado": empleado})


def editarEmpleado(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    telefono = request.POST['txtTelefono']
    correo = request.POST['txtCorreo']
    direccion = request.POST['txtDireccion']
    cargo = request.POST['txtCargo']

    empleado = Empleado.objects.get(codigo=codigo)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.telefono = telefono
    empleado.correo = correo
    empleado.direccion = direccion
    empleado.cargo = cargo
    empleado.save()

    return redirect('vistaEmpleados')


def eliminarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.delete()

    return redirect('vistaEmpleados')
