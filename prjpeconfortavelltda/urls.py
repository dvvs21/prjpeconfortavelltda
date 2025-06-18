"""
URL configuration for prjpeconfortavelltda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),

    
    path('produtos/', include("produtos.urls", namespace='produtos') ),
    path('cliente/', include("cliente.urls", namespace='clientes') ),
    path('contato/', include("contato.urls", namespace='contato') ),
    path('fornecedor/', include("fornecedor.urls", namespace='fornecedor') ),
    path('venda/', include("venda.urls", namespace='venda') ),
    path('login/', include("login.urls", namespace='login') ),
]

