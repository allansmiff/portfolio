from django.shortcuts import render
from portapp.forms import FormContact
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    form = FormContact(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            cidade = form.cleaned_data['cidade']
            estado = form.cleaned_data['estado']
            mensagem = form.cleaned_data['mensagem']
            messages.success(request, 'E-mail enviado com sucesso!')
        else:
            messages.error(request, "Falha ao enviar e-mail!")

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def services(request):
    return render(request, 'services.html')
