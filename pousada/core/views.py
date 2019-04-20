from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .forms import ContatoForm


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'index.html', context)


def servicos(request):
    return render(request, 'core/servicos.html')


def contato(request):
    return render(request, 'core/contato.html')


def contato_add(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(resolve_url('core:home'))
