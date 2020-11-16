from django.http import HttpResponse
from django.shortcuts import render
#from .forms import ContactoForm

def home_page(request):
  return render(request, "home_page.html")

def sobre_page(request):
  return render(request, "sobre_page.html")

def contacto_page(request):
	return render(request, "contacto_page.html")
  #if request.method == "POST":
   # print(request.POST)

  #formulario = ContactoForm()
  #return render(request, "contacto_page.html", {'formulario':formulario})