from django.urls import path 
from . import views 

urlpatterns = [
    path("<int:month>", views.months_by_number),
    
    path("<str:month>/", views.months)
    
]