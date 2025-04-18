from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def months(request, month):
    if month.lower() == "january":
        message_month = f"we are in {month}, we eat rice"
    elif month.lower() == "february":
        message_month = f"we are in {month}, we eat beans"
    elif month.lower() == "march":
        message_month = f"we are in {month}, we eat pineaple"
    else:
        return HttpResponseNotFound("your input is not in the first month")
    return HttpResponse(message_month)            
        