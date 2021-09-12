from django.shortcuts import render
from django.contrib import messages

from . import models

def index(request):
    return render(request, 'core/index.html', {})

def about(request):
    return render(request, 'core/about.html', {})

def bank(request):
    files = models.File.objects.all()

    return render(request, 'core/bank.html', {'files': files})

def contact(request):
    if request.method == 'POST':
        try:
            models.ContactForm.objects.create(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                phone_number = request.POST.get('phone'),
                message = request.POST.get('message'),
            )

            messages.success(request, 'Mensagem enviada com sucesso.')
        except:
            messages.error(request, 'Não foi possível enviar a mensagem. Por favor, tente novamente.')
            
    return render(request, 'core/contact.html', {})
