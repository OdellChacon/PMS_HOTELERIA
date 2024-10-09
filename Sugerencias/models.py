from django.db import models

# Create your models here.

stars = [
    [0, "★"],
    [1, "★★"],
    [2, "★★★"],
    [3, "★★★★"],
    [4, "★★★★★"],
]


class Sugerencias(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Cedula = models.CharField(max_length=8)
    Telefono = models.CharField(max_length=11)
    Experiencia = models.TextField()
    Clasificacion = models.IntegerField(choices=stars, blank=True)

    def __str__(self):
        return self.Nombre + " " + self.Apellido
