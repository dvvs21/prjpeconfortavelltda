from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100, help_text='Informe seu nome completo')
    email = models.CharField(max_length=100, help_text='Informe seu e-mail')
    telefone = models.CharField(max_length=11, help_text='Informe seu telefone com apenas números, sem espaços ou traços')
    hora_contato = models.CharField(max_length=10, help_text='Qual turno deseja ser contatado? (manhã, tarde ou noite)')
    mensagem = models.CharField(max_length=1024, help_text='Escreva sua mensagem ou dúvida')
    
    def __str__(self):
        return f'Contato de {self.nome} - {self.email}'