from django.db import models
# Create your models here.

seccion = [
    [0, "Desayuno"],
    [1, "Almuerzo"],
    [2, "Postre"],
    [3, "Bebida"],
    [4, "Cena"],
]


class Producto(models.Model):
    Producto = models.CharField(max_length=20)
    Descripcion = models.TextField()
    TipoProducto = models.IntegerField(choices=seccion)
    Precio = models.IntegerField()
    Promocion = models.BooleanField(default=False)
    Imagen = models.ImageField(upload_to="restaurante", null=True)

    def __str__(self):
        return self.Producto
