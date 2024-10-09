from django import forms
from .models import Producto


class ProductoFrm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
