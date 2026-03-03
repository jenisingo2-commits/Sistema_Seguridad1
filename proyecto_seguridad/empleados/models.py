from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    clave = models.CharField(max_length=20)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    from django.db import models
from django.contrib.auth.models import User

class PreguntaSeguridad(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pregunta1 = models.CharField(max_length=255)
    respuesta1 = models.CharField(max_length=255)
    pregunta2 = models.CharField(max_length=255)
    respuesta2 = models.CharField(max_length=255)

    def __str__(self):
        return f"Preguntas de seguridad de {self.usuario.username}"