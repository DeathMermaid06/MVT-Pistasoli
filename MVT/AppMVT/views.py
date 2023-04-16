from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente, Pedido, Factura
from .forms import ClienteForm


# Create your views here.

def inicioApp(request):
    return render(request, ("AppMVT/inicio.html"))

def inicio(request):
    return (HttpResponse("inicioApp"))

def clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = form.cleaned_data["nombre"]
            cliente.apellido = form.cleaned_data["apellido"]
            cliente.telefono = form.cleaned_data["telefono"]
            cliente.save()
    else:
       form = ClienteForm() 

    clientes = Cliente.objects.all()
    context= {"clientes": clientes, "form": form}
    return render(request, ("AppMVT/cliente.html"), context)

def pedidos(request):
    return render(request, ("AppMVT/pedido.html"))

def facturas(request):
    return render(request, ("AppMVT/factura.html"))

