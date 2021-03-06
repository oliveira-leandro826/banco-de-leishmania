# Generated by Django 3.2.6 on 2021-08-08 21:55

import core.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nome')),
                ('email', models.CharField(max_length=256, verbose_name='E-mail')),
                ('phone_number', models.CharField(max_length=256, verbose_name='Telefone')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Formulário de Contato',
                'verbose_name_plural': 'Formulários de Contato',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nome')),
                ('file', models.FileField(upload_to=core.models.path, verbose_name='Arquivo')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
