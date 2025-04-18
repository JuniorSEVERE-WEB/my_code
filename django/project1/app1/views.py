from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def months(request, month):
    return HttpResponse(f"we are in {month}")