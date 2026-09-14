from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Producto

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, activo=True)
    context = {
        'producto': producto,
    }
    return render(request, 'app1/detalle.html', context)

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