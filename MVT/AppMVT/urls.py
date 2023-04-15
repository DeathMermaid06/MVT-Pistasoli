from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/', clientes, name="clientes"),
    path('factura/', facturas, name="facturas"),
    path('pedido/', pedidos, name="pedidos"),
    path('', inicioApp, name="inicioApp"),

]

