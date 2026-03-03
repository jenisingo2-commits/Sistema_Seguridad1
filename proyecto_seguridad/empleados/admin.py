from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'sueldo', 'apellido', 'fecha_ingreso') 

from django.contrib import admin
from .models import PreguntaSeguridad

admin.site.register(PreguntaSeguridad)   