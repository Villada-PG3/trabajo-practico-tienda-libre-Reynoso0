from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('sobre_mi/', views.sobre_mi),
]