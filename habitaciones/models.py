from django.db import models

# Create your models here.


class categorias(models.Model):
    can_pers = models.PositiveIntegerField()
    nombre_c = models.CharField(max_length=15, blank=False, null=False)
    categoria = models.TextField(null=True)
    precioxdia = models.PositiveIntegerField()
    foto = models.ImageField(upload_to="images/", null=True,blank=True)
    estatus_categ = models.PositiveIntegerField(null=True)
    
class habitaciones(models.Model):
    id_num_habitaciones = models.BigAutoField(auto_created=False, primary_key=True, serialize=False)
    id_categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=False)
    numero_habitacion = models.PositiveIntegerField(null=True)
    estatus_habi = models.PositiveIntegerField(null=True)