from django.urls import path
from . import views 

app_name = 'login'

urlpatterns = [
    path('login', views.logar, name="login"),
   
]