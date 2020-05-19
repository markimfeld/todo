from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world!")

def marcos(request):
    return HttpResponse("Hello, Marcos!")

def greeting(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}')