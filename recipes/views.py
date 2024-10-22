from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse(render(request,'recipes/pages/home.html', context={
        'nome':'Renan',
        'idade':'20',
        'signo':'Capricórnio'
    }))

def recipe(request, id):
    return HttpResponse(render(request,'recipes/pages/recipe-view.html', context={
        'nome':'Renan',
        'idade':'20',
        'signo':'Capricórnio'
    }))
