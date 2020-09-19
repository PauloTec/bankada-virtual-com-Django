from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	html_ = "codigo bootstrap ficará aqui!"

	return HttpResponse(html_)