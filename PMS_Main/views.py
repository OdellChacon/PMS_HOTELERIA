from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def index(request):
    return render(request, "index.html")


def registro(request):
    if (request.method == "GET"):
        return render(request, "registro.html", {
            'forms': UserCreationForm
        })
    else:
        if (request.POST["password1"] == request.POST["password2"]):
            try:
                osvell = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                osvell.save()
                login(request, osvell)
                return redirect("dashboard")
            except IntegrityError:
                return render(request, "registro.html", {
                    'forms': UserCreationForm,
                    'error': "Error: (Usuario ya Existente)"
                })
        else:
            return render(request, "registro.html", {
                'forms': UserCreationForm,
                'error': "Error: (Las Contraseñas NO Coinciden)"
            })


def cerrar_sesion(request):
    logout(request)
    return redirect('Home')
