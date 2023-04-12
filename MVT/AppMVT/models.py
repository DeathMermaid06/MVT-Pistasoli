from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()

class Pedido(models.Model):
    idCliente=models.IntegerField()
    sabor=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    fecha=models.DateField()

class Factura(models.Model):
    idCliente=models.IntegerField()
    monto=models.CharField(max_length=50)
    liquidado=models.BooleanField()
    fecha=models.DateField()

