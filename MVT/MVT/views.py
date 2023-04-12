from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return(HttpResponse("esto funciona"))

def dos(request):
    return(HttpResponse("esto funciona dos"))

def saludo_nombre(request, nombre):
    return HttpResponse(f"este es tu nombre: {nombre}")

"""
def probandohtml(request):

    diccionario={"Nombre":"Jose", "Apellido":"Perez", "Edad":32, "lista":[1,2,5,6,3,4]}

    archivo=open(r'/Users/marie/Documents/GitHub/MVTPistasoli/Plantillas/template1.html')
    texto=archivo.read()
    archivo.close()
    template=Template(texto)
    contexto=Context(diccionario)
    documento=template.render(contexto)
    return HttpResponse(documento)
"""

def probandohtmlloader(request):

    diccionario={"Nombre":"Jose", "Apellido":"Perez", "Edad":32, "lista":[1,2,5,6,3,4]}
   
    template=loader.get_template("template1.html")
    documento=template.render(diccionario)
    return HttpResponse(documento)