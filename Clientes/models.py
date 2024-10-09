from django.db import models

# Create your models here.


class Cliente(models.Model):
    Cedula = models.CharField(max_length=8)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Telefono = models.CharField(max_length=11)
    Correo = models.EmailField()
    Direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre + " " + self.Apellido
