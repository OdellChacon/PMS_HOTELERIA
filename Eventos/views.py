from django.shortcuts import render

# Create your views here.


def verEventos(request):
    return render(request, "verEventos.html")
