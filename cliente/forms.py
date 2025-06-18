from django import forms
from .models import Cliente

class ClienteForm(forms.Form):
    nome = forms.CharField(max_length=70, required=True, help_text='Informe o nome completo do cliente')
    cpf = forms.CharField(max_length=11, required=True, help_text='Informe o CPF do cliente')
    endereco = forms.CharField(max_length=100, required=True, help_text='Informe o endereço do cliente')
    cidade = forms.CharField(max_length=50, help_text='Informe o nome da sua cidade',required=True)
    telefone = forms.CharField(max_length=11, required=True, help_text='Informe o telefone do cliente')
    estado_domicilio = forms.CharField(max_length=2, required=True, help_text='Informe o estado de domicílio do cliente')
    contato = forms.CharField(max_length=1, required=True)
    email = forms.CharField(max_length=100, required=True)
    genero = forms.CharField(max_length=1, required=True)
    contato = forms.CharField(max_length=1, required=True)
    email = forms.CharField(max_length=100, help_text='Informe seu e-mail', required=False)
    
    

class ClienteAtualizarForm(forms.ModelForm):
    nome = forms.CharField(max_length=70, required=True, help_text='Informe o nome completo do cliente')
    cpf = forms.CharField(max_length=11, required=True, help_text='Informe o CPF do cliente')
    endereco = forms.CharField(max_length=100, required=True, help_text='Informe o endereço do cliente')
    telefone = forms.CharField(max_length=11, required=True, help_text='Informe o telefone do cliente')
    estado_domicilio = forms.CharField(max_length=2, required=True, help_text='Informe o estado de domicílio do cliente')
    email = forms.CharField(max_length=100, required=True)
    genero = forms.CharField(max_length=1, required=True)
    contato = forms.CharField(max_length=1, required=True)
    email = forms.CharField(max_length=100, help_text='Informe seu e-mail', required=False)