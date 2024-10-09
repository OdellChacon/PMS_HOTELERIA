from django.db import models

# Create your models here.

class Huesped(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11, blank=True)
    correo = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=30, blank=True)
    cargo = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.nombre + ' - ' + self.codigo