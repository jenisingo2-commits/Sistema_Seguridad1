# models.py
from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('supervisor', 'Supervisor'),
        ('operario', 'Operario'),
        ('seguridad', 'Seguridad'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES, default='operario')
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()
    
    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"

class Pago(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_pago = models.DateField(auto_now_add=True)
    salario_neto = models.DecimalField(max_digits=10, decimal_places=2)
    bonificaciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def calcular_total(self):
        return self.salario_neto + self.bonificaciones - self.deducciones
    
    def __str__(self):
        return f"Pago {self.empleado} - {self.fecha_pago}"