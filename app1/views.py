from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto


def home(request):
    productos_destacados = Producto.objects.filter(activo=True).order_by('-fecha_creacion')[:3]
    context = {
        'productos_destacados': productos_destacados,
        'nombre_tienda': 'Mi tienda',
    }
    return render(request, 'app1/home.html', context)

def sobre_mi(request):
    return render(request, 'app1/sobre_mi.html')


def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by('nombre')
    context = {
        'productos': productos,
    }
    return render(request, 'app1/catalogo.html', context)