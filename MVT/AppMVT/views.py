from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inicio(request):
    return (HttpResponse("inicio"))

def cliente(request):
    return (HttpResponse ("Cliente"))

def pedido(request):
    return (HttpResponse ("Pedido"))

def factura(request):
    return (HttpResponse ("Factura"))

