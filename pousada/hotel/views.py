from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .models import Pessoa
from .forms import PessoaForm


@login_required
def dashboard(request):
    return render(request, 'hotel/dashboard.html')


@login_required
def pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {
        'pessoas': pessoas,
        'form': form,
    }
    return render(request, 'hotel/pessoas.html', data)


@login_required
def pessoas_detail(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    data = {'pessoa': pessoa}
    return render(request, 'hotel/pessoas_detail.html', data)


@login_required
def pessoas_edit(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('hotel:pessoas'))
    data = {
        'pessoa': pessoa,
        'form': form,
    }
    return render(request, 'hotel/pessoas_editar.html', data)


@login_required
def pessoas_delete(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    pessoa.delete()
    return HttpResponseRedirect(resolve_url('hotel:pessoas'))


@login_required
def pessoas_add(request):
    form = PessoaForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(resolve_url('hotel:pessoas'))


@login_required
def quartos(request):
    return render(request, 'hotel/quartos.html')


@login_required
def rotativos(request):
    return render(request, 'hotel/rotativos.html')


@login_required
def mensalistas(request):
    return render(request, 'hotel/mensalistas.html')
