from django.http import HttpResponse 
from django.template import Template, Context
#ejemplo de vista 

def Inicio(request):
    #Abrimos el documento que contiene la plantilla
    PlantillaInicio = open("prueba2/plantillas/index.html")
    #cargamos el documento en una variable de tipo 'Template'
    template = Template(PlantillaInicio.read())
    #Cerramos el documento externo 
    PlantillaInicio.close()
    #crear un contexto
    contexto = Context()
    #Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

