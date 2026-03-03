from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PreguntaSeguridadForm
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Bienvenido al Sistema de Seguridad")


@login_required
def configurar_preguntas(request):
    if request.method == 'POST':
        form = PreguntaSeguridadForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.usuario = request.user
            pregunta.save()
            return redirect('inicio')  # cambié 'home' por 'inicio'
    else:
        form = PreguntaSeguridadForm()

    return render(request, 'configurar_preguntas.html', {'form': form})