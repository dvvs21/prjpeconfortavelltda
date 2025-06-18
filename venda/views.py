from django.shortcuts import render

# Create your views here.
def registrar(request):
    return render(request, 'venda/registrovenda.html')

def listar(request):
    return render(request, 'venda/listavenda.html')