from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

months_dict = {
    "january": "we eat rice",
    "february": "We eat beans",
    "march": "we eat pinneaple",
    "april": "We are in april",
    "may": "we are in may",
    "june": "we are in june",
    "july": "we are in july",
    "august": "we are in august",
    "september": "we are in september",
    "october": " we are in october",
    "november": "we are in november",
    "december": "we are in december"
}
# Create your views here.

def months_by_number(request, month):
    return HttpResponse(month)


def months(request, month):
    try:
        
        message_month = months_dict[month.lower()]
        return HttpResponse(message_month)
          
    except KeyError:
        return HttpResponseNotFound("This month is not supported, okok!")    
   
             
        