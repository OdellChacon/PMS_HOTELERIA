from django import forms
from .models import Stock, artLimpieza, artHabitaciones, Proveedores


class IngredientesFrm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class LimpiezaFrm(forms.ModelForm):
    class Meta:
        model = artLimpieza
        fields = '__all__'


class HabitacionesFrm(forms.ModelForm):
    class Meta:
        model = artHabitaciones
        fields = '__all__'


class ProveedorFrm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'
