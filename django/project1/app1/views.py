from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}
# Create your views here.

def index(request):
    months = list(months_dict.keys())
    return render(request, "app1/index.html", {
        "months": months
    })

def months_by_number(request, month):
    the_months = list(months_dict.keys())
    
    if month > len(the_months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = the_months[month - 1]
    redirect_path = reverse("month-app1", args=[redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path)


def months_by_string(request, month):
    try:
        print("Mois reçu :", month)  # Debug : vérifiez la valeur dans la console
        message_month = months_dict[month.lower()]  # Si le mois est valide
        return render(request, "app1/app.html", {
            "text": message_month,
            "month_name": month})
    except:
        raise Http404()
"""
months_by_number : Gère la conversion nombre → nom

months_by_string : Gère l'affichage final  
"""             
        