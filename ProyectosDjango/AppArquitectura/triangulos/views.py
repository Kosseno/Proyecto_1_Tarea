from django.shortcuts import render
import math
import sys
import os

# triangulo.py la carpeta padre
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from triangulo import triangulorectangulo

def calculadora_triangulos(request):
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            base = float(request.POST.get('base'))
            altura = float(request.POST.get('altura'))
            
            # instancia del triángulo
            triangulo = triangulorectangulo(base, altura)
            
            # Calculo
            resultado = {
                'base': base,
                'altura': altura,
                'area': round(triangulo.calcular_area(), 2),
                'hipotenusa': round(triangulo.calcular_hipotenusa(), 2),
                'perimetro': round(triangulo.calcular_perimetro(), 2),
            }
        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = f"Error al procesar los datos: {str(e)}"
    
    context = {
        'resultado': resultado,
        'error': error,
    }
    return render(request, 'triangulos/index.html', context)
