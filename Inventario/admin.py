from django.contrib import admin
from .models import Stock, Proveedores, artLimpieza, artHabitaciones
# Register your models here.

admin.site.register(Stock)
admin.site.register(Proveedores)
admin.site.register(artLimpieza)
admin.site.register(artHabitaciones)
