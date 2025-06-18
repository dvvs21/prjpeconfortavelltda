from django import forms
from .models import Fornecedor

class FornecedorForm(forms.Form):
    codigo = forms.IntegerField(help_text='Informe o Código do fabricante', required=True)
    nome = forms.CharField(max_length=70, help_text='Informe o nome do fabricante', required=True)