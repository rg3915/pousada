from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .forms import ContatoForm


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'index.html', context)


def servicos(request):
    return render(request, 'core/servicos.html')


def contato(request):
    form = ContatoForm()
    template_name = 'core/contato.html'
    context = {'form': form}
    return render(request, template_name, context)


def contato_add(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('core:contato_confirmacao'))


def contato_confirmacao(request):
    template_name = 'core/contato_confirmacao.html'
    return render(request, template_name)
