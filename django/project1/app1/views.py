from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    list_items = ""
    the_months = list(months_dict.keys())##
    
    for month in the_months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-app1", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
            "month_name": month.capitalize()})
    except KeyError:
        return HttpResponseNotFound("<h1>Ce mois n'est pas valide !</h1>")
    except Exception as e:
        print("Erreur de template :", e)  # Debug : vérifiez si le template est manquant
        return HttpResponseNotFound("<h1>Erreur de chargement du template</h1>")  
   
"""
months_by_number : Gère la conversion nombre → nom

months_by_string : Gère l'affichage final  
"""             
        