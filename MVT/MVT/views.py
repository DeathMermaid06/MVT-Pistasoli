from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return(HttpResponse("esto funciona"))

def dos(request):
    return(HttpResponse("esto funciona dos"))

def saludo_nombre(request, nombre):
    return HttpResponse(f"este es tu nombre: {nombre}")

def probandohtml(request):
    archivo=open(r'/Users/marie/Documents/GitHub/MVTPistasoli/Plantillas/template1.html')
    texto=archivo.read()
    archivo.close()
    template=Template(texto)
    contexto=Context()
    documento=template.render(contexto)
    return HttpResponse(documento)