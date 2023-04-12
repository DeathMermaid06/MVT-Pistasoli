from django.shortcuts import render
from .models import cliente, pedido, factura
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    HttpResponse("inicio")

def cliente(request):
    return HttpResponse ("Cliente")

def pedido(request):
    return HttpResponse ("Pedido")

def factura(request):
    return HttpResponse ("Factura")

