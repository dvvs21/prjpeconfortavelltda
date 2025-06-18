from django import forms 
from .models import Contato

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, help_text='Informe seu nome completo')
    email = forms.CharField(max_length=100, help_text='Informe seu e-mail')
    telefone = forms.CharField(max_length=11, help_text='Informe seu telefone com apenas números, sem espaços ou traços')
    hora_contato = forms.CharField(max_length=10, help_text='Qual turno deseja ser contatado? (manhã, tarde ou noite)')
    mensagem = forms.CharField(max_length=1024, help_text='Escreva sua mensagem ou dúvida')