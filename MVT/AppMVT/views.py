from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inicioApp(request):
    return render(request, ("AppMVT/inicio.html"))

def inicio(request):
    return (HttpResponse("inicioApp"))

def cliente(request):
    return render(request, ("AppMVT/cliente.html"))

def pedido(request):
    return render(request, ("AppMVT/pedido.html"))

def factura(request):
    return render(request, ("AppMVT/factura.html"))

