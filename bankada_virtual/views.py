from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
  return render(request, "home_page.html")

def sobre_page(request):
  return render(request, "sobre_page.html")

def contacto_page(request):
  return render(request, "contacto_page.html")