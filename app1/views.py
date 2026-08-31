from django.shortcuts import render


def home(request):
    productos_destacados = [
        {
            'nombre': 'Mouse',
            'precio': 15000,
            'descripcion': 'Mouse óptico para computadora'
        },
        {
            'nombre': 'Teclado',
            'precio': 25000,
            'descripcion': 'Teclado para computadora'
        },
        {
            'nombre': 'Monitor',
            'precio': 120000,
            'descripcion': 'Monitor LED de 24 pulgadas'
        },
        {
            'nombre': 'Auriculares',
            'precio': None,
            'descripcion': 'Auriculares con micrófono'
        },
        {
            'nombre': 'Webcam',
            'precio': 45000,
            'descripcion': 'Cámara web para computadora'
        },
        {
            'nombre': 'Parlante',
            'precio': 35000,
            'descripcion': 'Parlante para computadora'
        },
]
    context = {
        'productos_destacados': productos_destacados,
        'nombre_tienda': 'Mi tienda',
    }

    return render(request, 'app1/home.html', context)


def sobre_mi(request):
    return render(request, 'app1/sobre_mi.html')