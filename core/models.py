from django.db import models
from django.utils import timezone
from uuid import uuid4
import os

def path(instance, filename):
    extension = filename.split('.')[-1]
    
    file_name = '{}.{}'.format(uuid4().hex, extension)

    return os.path.join('arquivos/', file_name)

class File(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=256, blank=False, null=False)
    file = models.FileField(verbose_name='Arquivo', upload_to=path, blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)
    
    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

class ContactForm(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=256, blank=False, null=False)
    email = models.CharField(verbose_name='E-mail', max_length=256, blank=False, null=False)
    phone_number = models.CharField(verbose_name='Telefone', max_length=256, blank=False, null=False)
    message = models.TextField(verbose_name='Mensagem', blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='Data de criação', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contato'