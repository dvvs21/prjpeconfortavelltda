from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm, ClienteAtualizarForm

# Create your views here.

def cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            dados_cliente = form.cleaned_data
            cliente_obj = Cliente(
                nome = dados_cliente['nome'],
                cpf = dados_cliente['cpf'],
                endereco = dados_cliente ['endereco'],
                telefone = dados_cliente['telefone'],
                estado_domicilio = dados_cliente['estado_domicilio'],
                cidade = dados_cliente['cidade'],
                genero = dados_cliente['genero'],
                contato = dados_cliente['contato'],
                email = dados_cliente ['email'],
            )
            cliente_obj.save()
        return redirect('clientes:listar')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastroclt.html', {'form': form})

def listar(request):
    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes
    }
    return render(request, 'clientes/listaclt.html', context=contexto)


def cadastro(request):
    return render(request, 'clientes/cadastroclt.html')





def exclui(request, cpf):
    excluir_cliente = Cliente.objects.get(cpf=cpf)
  
    excluir_cliente.delete()

    return redirect('clientes:listar')


def carregar_cliente(request, cpf):
    cliente = Cliente.objects.get(cpf=cpf)
    contexto = {
        'clientes': cliente,
    }

    return render (request, 'clientes/atualizarCliente.html', context=contexto)
    
    

def atualizar_cliente (request):
    if request.method == 'POST':
        form = ClienteAtualizarForm(request.POST)
        if form.is_valid():
            dados_cliente = form.cleaned_data
            cpf = dados_cliente['cpf']
            cliente = Cliente.objects.get(cpf=cpf)
            cliente.nome = dados_cliente['nome']
            cliente.endereco = dados_cliente['endereco']
            cliente.telefone = dados_cliente['telefone']
            cliente.email = dados_cliente['email']
            Cliente.save()
            
        else: 
            print (form.errors)
    return redirect('cliente:listar')