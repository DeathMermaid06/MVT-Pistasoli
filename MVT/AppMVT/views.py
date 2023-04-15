from django.http import HttpResponse
from django.shortcuts import render
from .models import cliente, pedido, factura


# Create your views here.

def inicioApp(request):
    return render(request, ("AppMVT/inicio.html"))

def inicio(request):
    return (HttpResponse("inicioApp"))

def clientes(request):
    clientes = cliente.objects.all()
    context= {"clientes": clientes}
    return render(request, ("AppMVT/cliente.html"), context)

def pedidos(request):
    return render(request, ("AppMVT/pedido.html"))

def facturas(request):
    return render(request, ("AppMVT/factura.html"))

