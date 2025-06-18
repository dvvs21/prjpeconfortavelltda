from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    codigo = models.AutoField(primary_key=True, help_text='Informe o Código do fabricante')
    nome = models.CharField(max_length=70, help_text='Informe o nome do fabricante')

    def __str__(self):
        return f'{self.nome}'