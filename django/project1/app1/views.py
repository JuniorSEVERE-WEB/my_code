from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("we are in january")

def february(request):
    return HttpResponse("We are in february")

def march(request):
    return HttpResponse("We are in march")