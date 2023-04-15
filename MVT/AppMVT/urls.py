from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/', cliente, name="clientes"),
    path('factura/', factura, name="facturas"),
    path('pedido/', pedido, name="pedidos"),
    path('', inicioApp, name="inicioApp"),

]

