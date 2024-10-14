from django.shortcuts import render, HttpResponse

menu= """
    <a href="/">Home</a>
    <a href="/modulo">modulo</a>
    
"""
 # Create your views here.
def principal(request):
    contenido="<h2> Desarrollo web integral :)))</h2> <h3> Abigail Alejo Pineda </h3>"
    return HttpResponse(menu + contenido)

def modulo(request):
    contenido="<h2> aloja </h2> "
    return HttpResponse(menu + contenido)