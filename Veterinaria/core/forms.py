from django import forms
from django.forms import ModelForm
from .models import Contacto, Mascota





class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'