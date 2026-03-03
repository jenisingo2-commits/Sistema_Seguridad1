from django import forms
from .models import PreguntaSeguridad

class PreguntaSeguridadForm(forms.ModelForm):
    class Meta:
        model = PreguntaSeguridad
        fields = ['pregunta1', 'respuesta1', 'pregunta2', 'respuesta2']
        widgets = {
            'respuesta1': forms.PasswordInput(),
            'respuesta2': forms.PasswordInput(),
        }