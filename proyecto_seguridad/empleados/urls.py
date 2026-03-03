from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('preguntas/', views.configurar_preguntas, name='preguntas'),
]
