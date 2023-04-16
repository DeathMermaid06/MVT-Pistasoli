from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/', clientes, name="clientes"),
    path('factura/', facturas, name="facturas"),
    path('pedido/', pedidos, name="pedidos"),
    path('buscar/', buscar, name="buscar"),
    path('buscando/', buscando, name="buscando"),
    path('', inicioApp, name="inicioApp"),

]

