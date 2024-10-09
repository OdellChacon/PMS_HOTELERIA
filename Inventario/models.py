from django.db import models

# Create your models here.

semana = [
    [0, "Lunes"],
    [1, "Martes"],
    [2, "Miercoles"],
    [3, "Jueves"],
    [4, "Viernes"],
    [5, "Sabado"],
    [6, "Domingo"],
]

moneda = [
    [0, "Bolivares"],
    [1, "Dolares"],
    [2, "Pago Movil"],
    [3, "Pesos Colombianos"],
]


class Proveedores(models.Model):
    Proveedor = models.CharField(max_length=20)
    NombreContacto = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=20)
    Telefono = models.CharField(max_length=20)
    Correo = models.EmailField()
    Pago = models.IntegerField(choices=moneda)
    DiaEntregas = models.IntegerField(choices=semana)

    def __str__(self):
        return self.Proveedor


sistemaUnidades = [
    [0, 'Gramos'],
    [1, 'Kilogramos'],
    [2, 'Miligramos'],
    [3, 'Litros']
]

producType = [
    [0, "Granos"],
    [1, "Verduras"],
    [2, "Frutas"],
    [3, "Prod. Lacteos"],
    [4, "Proteinas"],
    [5, "Carne"],
    [6, "Otro"]
]


class Stock(models.Model):
    Codigo = models.IntegerField(max_length=5)
    Producto = models.CharField(max_length=20)
    Cantidad = models.IntegerField(max_length=5)
    Unidad = models.IntegerField(choices=sistemaUnidades)
    Tipo = models.IntegerField(choices=producType)
    Precio = models.IntegerField(max_length=5)
    Proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.Producto


limpieza = [
    [0, "Gramos"],
    [1, "Kilogramos"],
    [2, "Litros"],
    [3, "Ninguna de las anteriores"],
]


class artLimpieza(models.Model):
    Codigo = models.IntegerField(max_length=5)
    Producto = models.CharField(max_length=20)
    Cantidad = models.IntegerField(max_length=5)
    Unidad = models.IntegerField(choices=limpieza)
    Proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)

    def __str__(self):
        return self.Producto


class artHabitaciones(models.Model):
    Codigo = models.IntegerField(max_length=5)
    Producto = models.CharField(max_length=20)
    Cantidad = models.IntegerField(max_length=5)

    def __str__(self):
        return self.Producto
