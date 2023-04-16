from django import forms

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    telefono=forms.IntegerField()

class PedidoForm(forms.Form):
    idCliente=forms.IntegerField()
    sabor=forms.CharField(max_length=50)
    cantidad=forms.IntegerField()
    fecha=forms.DateField()

class FacturaForm(forms.Form):
    idCliente=forms.IntegerField()
    monto=forms.CharField(max_length=50)
    liquidado=forms.BooleanField()
    fecha=forms.DateField()