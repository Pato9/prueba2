from django.http import HttpResponse 

#ejemplo de vista 
def Inicio(request):
    text = "Hola mundo"
    return HttpResponse(text)