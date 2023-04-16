from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente, Pedido, Factura
from .forms import ClienteForm, PedidoForm, FacturaForm


# Create your views here.

def inicioApp(request):
    return render(request, ("AppMVT/inicio.html"))

def inicio(request):
    return (HttpResponse("inicioApp"))

def buscar(request):
    return render(request, ("AppMVT/buscar.html"))

def buscando(request):
    b_sabor=request.GET["sabor"]
    if b_sabor!="":
        pedidos=Pedido.objects.filter(sabor__icontains=b_sabor)
        print(pedidos)
        return render(request, "AppMVT/buscando.html", {"pedidos": pedidos})
    else:
       return render(request, ("AppMVT/buscar.html"))

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
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = Pedido()
            pedido.idCliente = form.cleaned_data["idCliente"]
            pedido.sabor = form.cleaned_data["sabor"]
            pedido.cantidad = form.cleaned_data["cantidad"]
            pedido.fecha = form.cleaned_data["fecha"]
            pedido.save()
    else:
       form = PedidoForm() 

    pedidos = Pedido.objects.all()
    context= {"pedidos": pedidos, "form": form}
    return render(request, ("AppMVT/pedido.html"), context)

def facturas(request):
    if request.method == "POST":
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = Factura()
            factura.idCliente = form.cleaned_data["idCliente"]
            factura.monto = form.cleaned_data["monto"]
            factura.liquidado = form.cleaned_data["liquidado"]
            factura.fecha = form.cleaned_data["fecha"]
            factura.save()
    else:
       form = FacturaForm() 

    facturas = Factura.objects.all()
    context= {"facturas": facturas, "form": form}
    return render(request, ("AppMVT/factura.html"), context)

