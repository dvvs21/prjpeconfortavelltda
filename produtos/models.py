from django.db import models

# Create your models here.
class Produto(models.Model):
    codigo = models.AutoField(primary_key=True, help_text='Código único do produto')
    nome = models.CharField(max_length=70, help_text='Informe o nome do produto')
    preco_compra = models.FloatField(help_text='Informe o preço de compra do produto')
    preco_venda = models.FloatField(help_text='Informe o preço de venda do produto')
    cor = models.CharField(max_length=20, help_text='Informe a cor do produto')
    dt_fabricacao = models.DateField(help_text='Informe a data de fabricação do produto')
    imagem = models.CharField(max_length=25, help_text='Informe o nome da imagem do produto')
    
    def __str__(self):
        return f'{self.nome}'