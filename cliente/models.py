from django.db import models

# Create your models here.
class Cliente(models.Model):
    cpf = models.CharField(max_length=11, help_text='Informe seu CPF com apenas números, sem pontos ou traços')
    nome = models.CharField(max_length=70, help_text='Nome completo')
    endereco = models.CharField(max_length=100, help_text='Endereço completo')   
    telefone = models.CharField(max_length=11, help_text='Informe seu telefone com apenas números, sem espaços ou traços')
    estado_domicilio = models.CharField(max_length=2, help_text='Informe a sigla do seu estado, por exemplo: SP, RJ, MG')
    cidade = models.CharField(max_length=50, help_text='Informe o nome da sua cidade')
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')])
    contato = models.CharField(max_length=1, choices=[('C', 'Para carta'), ('E', 'Para e-mail'), ('T', 'Para telefone'), ('F', 'Para fax')])
    email = models.CharField(max_length=100, help_text='Informe seu e-mail')
    usuario = models.CharField(max_length=100, help_text='Confirme o e-mail informado')
    senha = models.CharField(max_length=256, help_text='Informe uma senha segura')
    
    def __str__(self):
        return f'Olá, {self.nome}'