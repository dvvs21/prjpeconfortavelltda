from django.urls import path
from . import views 

app_name = 'clientes'

urlpatterns = [
    path('lista/', views.listar, name="listar"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    # path('excluir/', views.excluir, name="excluir_cliente"),
    path('carregar_cliente/', views.carregar_cliente, name="carregar_cliente"),
    path('atualizar_cliente/', views.atualizar_cliente, name="atualizar_cliente"),
    ]