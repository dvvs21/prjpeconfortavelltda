from django.shortcuts import render, redirect
from .forms import FornecedorForm
from .models import Fornecedor

# Create your views here.
def listar(request):
    lista_fornecedor = Fornecedor.objects.all()
    contexto = {
        'fornecedor': lista_fornecedor
    }
    return render(request, 'fornecedores/listafrn.html')


def cadastrar(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            dados_fornecedor = form.cleaned_data
            cliente_obj = Fornecedor(
                codigo = dados_fornecedor['codigo'],
                nome = dados_fornecedor ['nome'],
            )
            cliente_obj.save()
        return redirect ('fornecedor:listar')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/cadastrofrn.html')