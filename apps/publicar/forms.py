from django import forms
from django.forms import ModelForm
from .models import Publicaciones

class PublicarForm(ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['titulo', 'descripcion', 'estado', 'categoria']
        widgets = {
            'estado' : forms.CheckboxInput(),  
        }

