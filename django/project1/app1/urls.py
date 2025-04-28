from django.urls import path 
from . import views 
#
urlpatterns = [
    path("<int:month>/", views.months_by_number),
    
    path("<str:month>/", views.months_by_string, name ="month-app1"),
    
    path("", views.index, name="index") # /app1/
    
]