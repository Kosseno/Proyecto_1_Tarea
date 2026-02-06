from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculadora_triangulos, name='calculadora'),
    path('calcular/', views.calculadora_triangulos, name='calcular'),
]
