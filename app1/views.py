from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html')
# Create your views here.
def sobre_mi(request):
    return render(request, 'app1/sobre_mi.html')