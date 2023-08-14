from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def menu(request):
    return HttpResponse("Menu page")

def specials(request):
    return HttpResponse(" Specials Page")

def meals(request):
    return HttpResponse(" Meals page")
