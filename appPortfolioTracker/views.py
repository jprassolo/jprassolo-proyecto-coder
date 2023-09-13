from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, Activos, Libro

# Create your views here.

####################################################################
### LANDING PAGE
####################################################################   
def index(request): 
    return render(request,"landing/landing.html")

def acerca(request): 
    return render(request,"landing/acerca.html")

def contacto(request): 
    return render(request,"landing/contacto.html")

def terminos(request): 
    return render(request,"landing/terminos.html")

def politica(request): 
    return render(request,"landing/politica.html")


####################################################################
### MAIN PAGE
####################################################################
def main(request):
    # return render(request,"admin/admin.html")
    return render(request,"admin/main.html")

####################################################################
### CRUDS
####################################################################
def iactivos(request):
    return render(request,"pages/activos.html")

def iportfolios(request):
    return render(request,"pages/portfolios.html")

def aportfolios(request, nombre, descripcion):
    p = Portfolio(nombre=nombre ,descripcion=descripcion)
    p.save()
    return HttpResponse(f"""
        <p> portfolio {nombre} - cartera de {descripcion}, creado con exito! </p>
    """)

def ilibros(request):
    return render(request,"pages/libros.html")