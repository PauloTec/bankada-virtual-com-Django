from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactoFormulario

def home_page(request):
  return render(request, "home_page.html")

def sobre_page(request):
  return render(request, "sobre_page.html")

def contacto_page(request):
	if request.method == "POST":
		form = ContactoFormulario(request.POST or None)
		# check whether it's valid:
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactoFormulario()
	return render(request, 'contacto_page.html', {'form': form})