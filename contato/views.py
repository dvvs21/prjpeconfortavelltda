from django.shortcuts import render, redirect
from .models import Contato
from .forms import ContatoForm

# Create your views here.
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            dados_contato = form.cleaned_data
            contato_obj = Contato(
                nome = dados_contato['nome'],
                email = dados_contato ['email'],
                telefone = dados_contato ['telefone'],
                hora_contato = dados_contato ['hora_contato'],
                mensagem = dados_contato ['mensagem'],
            )
            contato_obj.save()
        return redirect ('contato:contato')
    else:
        form = ContatoForm()
    return render(request, 'contato/contato.html', {'form': form})

