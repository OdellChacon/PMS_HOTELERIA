from django.db import models

# Create your models here.


class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'Gerente'),
        ('1', 'Administrador'),
        ('2', 'Recepcionista'),
        ('3', 'Encargado de Cocina'),
        ('4', 'Cocinero'),
        ('5', 'Personal de Mantenimiento'),
    )

    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    cargo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + ' - ' + self.codigo
