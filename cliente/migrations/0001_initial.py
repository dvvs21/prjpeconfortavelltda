# Generated by Django 5.2.1 on 2025-06-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(help_text='Informe seu CPF com apenas números, sem pontos ou traços', max_length=11)),
                ('nome', models.CharField(help_text='Nome completo', max_length=70)),
                ('endereco', models.CharField(help_text='Endereço completo', max_length=100)),
                ('telefone', models.CharField(help_text='Informe seu telefone com apenas números, sem espaços ou traços', max_length=11)),
                ('estado_domicilio', models.CharField(help_text='Informe a sigla do seu estado, por exemplo: SP, RJ, MG', max_length=2)),
                ('cidade', models.CharField(help_text='Informe o nome da sua cidade', max_length=50)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1)),
                ('contato', models.CharField(choices=[('C', 'Para carta'), ('E', 'Para e-mail'), ('T', 'Para telefone'), ('F', 'Para fax')], max_length=1)),
                ('email', models.CharField(help_text='Informe seu e-mail', max_length=100)),
                ('usuario', models.CharField(help_text='Confirme o e-mail informado', max_length=100)),
                ('senha', models.CharField(help_text='Informe uma senha segura', max_length=256)),
            ],
        ),
    ]
