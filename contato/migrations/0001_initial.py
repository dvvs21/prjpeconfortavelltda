# Generated by Django 5.2.1 on 2025-06-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Informe seu nome completo', max_length=100)),
                ('email', models.CharField(help_text='Informe seu e-mail', max_length=100)),
                ('telefone', models.CharField(help_text='Informe seu telefone com apenas números, sem espaços ou traços', max_length=11)),
                ('hora_contato', models.CharField(help_text='Qual turno deseja ser contatado? (manhã, tarde ou noite)', max_length=10)),
                ('mensagem', models.CharField(help_text='Escreva sua mensagem ou dúvida', max_length=1024)),
            ],
        ),
    ]
