from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    the_months = list(months_dict.keys())
    redirect_month = the_months[month - 1]
    return HttpResponseRedirect("/app1/" + redirect_month)


def months_by_string(request, month):
    try:
        
        message_month = months_dict[month.lower()]
        return HttpResponse(message_month)
          
    except:
        return HttpResponseNotFound("This month is not supported, okok!")    
   
             
        