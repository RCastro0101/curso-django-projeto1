from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse(render(request,'recipes/home.html', context={
        'nome':'Renan',
        'idade':'20',
        'signo':'Capricórnio'
    }))
