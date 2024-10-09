from django.contrib import admin
from .models import datos_reserva
from .models import reservaciones
from .models import metodos_pagos
admin.site.register(datos_reserva)
admin.site.register(reservaciones)
admin.site.register(metodos_pagos)
# Register your models here.
