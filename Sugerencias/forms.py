from django import forms
from .models import Sugerencias


class SugerenciasFrm(forms.ModelForm):
    class Meta:
        model = Sugerencias
        fields = '__all__'
