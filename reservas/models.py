from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from habitaciones.models import *

# Create your models here.
 
    
class datos_reserva(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(categorias, on_delete=models.CASCADE, null=True)
    f_entrada = models.DateField()
    f_salida = models.DateField()
    num_personas = models.PositiveIntegerField()
    num_niños = models.PositiveIntegerField()
    num_habi_solicitadas = models.PositiveIntegerField(null=True)
    estatus_datos_rese = models.PositiveIntegerField(null=True)
    dias_pago = models.PositiveIntegerField(null=True)
    n_ocupante = models.CharField(max_length=25, blank=False, null=True)


   
class metodos_pagos(models.Model):
    metodo = models.CharField(max_length=25, blank=False, null=False)
    descripcion= models.TextField(null=True)
    
class reservaciones(models.Model):
    id_datos_reserva = models.ForeignKey(datos_reserva, on_delete=models.CASCADE, null=True)
    id_num_habitaciones = models.ForeignKey(habitaciones, on_delete=models.CASCADE, null=True)
    nombre_r = models.CharField(max_length=25, blank=False, null=False)
    apellido_r = models.CharField(max_length=25, blank=False, null=False)
    telefono = models.PositiveIntegerField()
    Forma_pago = models.ForeignKey(metodos_pagos, on_delete=models.CASCADE, null=True)
    tarifa_pago =  models.PositiveIntegerField(null=True)
    fecha_reserva = models.DateField(null=True)
    hora_de_llegada = models.TimeField(null=True)
    estatus_reservacion = models.PositiveIntegerField(null=True)
    peticiones =  models.CharField(max_length=250, blank=False, null=True)
    disponible = models.BooleanField(default=False, null=True)
