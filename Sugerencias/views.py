from django.shortcuts import render, redirect, get_object_or_404
from .models import Sugerencias
from .forms import SugerenciasFrm
from django.contrib.auth.decorators import login_required
# Create your views here.


def newSugerencias(request):
    data = {
        'sugerencias': SugerenciasFrm()
    }

    if (request.method == "POST"):
        frm = SugerenciasFrm(data=request.POST)
        if frm.is_valid():
            frm.save()
            return redirect("/")

    return render(request, "LibroSugerencias.html", data)


@login_required
def verSugerencias(request):

    sugerencia = Sugerencias.objects.all()

    return render(request, "verSugerencias.html", {
        'clientes': sugerencia
    })


@login_required
def leerSugerencia(request, id):

    Kazuru = get_object_or_404(Sugerencias, id=id)

    data = {
        'sugerencia': SugerenciasFrm(instance=Kazuru)
    }

    if (request.method == "POST"):
        ZeroKardem = SugerenciasFrm(data=request.POST, instance=Kazuru)
        if ZeroKardem.is_valid():
            return redirect("leer")

    return render(request, "leerSugerencia.html", data)
