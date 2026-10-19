from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    path('catalogo/', views.CatalogoView.as_view(), name='catalogo'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
]