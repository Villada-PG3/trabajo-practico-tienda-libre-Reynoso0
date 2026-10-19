from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from django.views.generic import TemplateView, ListView


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, activo=True)
    context = {
        'producto': producto,
    }
    return render(request, 'app1/detalle.html', context)

class HomeView(TemplateView):
    template_name = 'app1/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_destacados'] = Producto.objects.filter(activo=True).order_by('-fecha_creacion')[:3]
        context['nombre_tienda'] = 'Mi tienda'
        return context

def sobre_mi(request):
    return render(request, 'app1/sobre_mi.html')


class CatalogoView(ListView):
    model = Producto
    template_name = 'app1/catalogo.html'
    context_object_name = 'productos'
    queryset = Producto.objects.filter(activo=True).order_by('nombre')