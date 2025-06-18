from django import forms
from .models import Produto


class ProdutoForm(forms.Form):
    codigo = forms.IntegerField(help_text='Código único do produto')
    nome = forms.CharField(max_length=70, help_text='Informe o nome do produto')
    preco_compra = forms.FloatField(help_text='Informe o preço de compra do produto')
    preco_venda = forms.FloatField(help_text='Informe o preço de venda do produto')
    cor = forms.CharField(max_length=20, help_text='Informe a cor do produto')
    dt_fabricacao = forms.DateField(help_text='Informe a data de fabricação do produto')
    imagem = forms.CharField(max_length=25, help_text='Informe o nome da imagem do produto')
    