from django.shortcuts import render, HttpResponse

 # Create your views here.
def principal(request):
    contenido="<h2> Desarrollo web integral :)))</h2> <h3> Abigail Alejo Pineda </h3>"
    return HttpResponse(contenido)