from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
def cadastrar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            dados_produto = form.cleaned_data
            produto_obj = Produto(
                nome = dados_produto ['nome'],
                preco_compra = dados_produto ['preco_compra'],
                preco_venda = dados_produto ['preco_venda'],
                cor =  dados_produto ['cor'],
                dtfabricacao= dados_produto ['dtfabricacao'],
                imagem = dados_produto ['imagem'],
            )
            produto_obj.save()

        return redirect(request, 'produtos/listaprd.html')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastroprd.html', {'form': form})

def listar(request):
    produtos = Produto.objects.all()
    contexto = {
        'produtos': produtos
    }
    return render(request, 'produtos/listaprd.html', context=contexto)


