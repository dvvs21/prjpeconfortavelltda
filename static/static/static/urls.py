from django.urls import path 
from . import views

urlpatterns = [ 
    path("", views.static, name="static"),
    ]