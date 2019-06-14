from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .models import Pessoa
from .forms import PessoaForm, MovRotativoForm


@login_required
def dashboard(request):
    return render(request, 'hotel/dashboard.html')


@login_required
def pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()

    # Search
    search = request.GET.get('search')
    if search:
        pessoas = pessoas.filter(
            Q(nome__icontains=search,) |
            Q(cpf__icontains=search,)
        )
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


# @login_required
# def quartos_add(request):
#     pass


# @login_required
# def quartos_detail(request):
#     pass


# @login_required
# def quartos_edit(request):
#     pass


# @login_required
# def quartos_delete(request):
#     pass


@login_required
def rotativos(request):
    return render(request, 'hotel/rotativos.html')


@login_required
def rotativos_add(request):
    form = MovRotativoForm()
    template_name = 'hotel/rotativos_add.html'
    context = {'form': form}
    return render(request, template_name, context)


# @login_required
# def rotativos_detail(request):
#     pass


# @login_required
# def rotativos_edit(request):
#     pass


# @login_required
# def rotativos_delete(request):
#     pass


@login_required
def mensalistas(request):
    return render(request, 'hotel/mensalistas.html')


# @login_required
# def mensalistas_add(request):
#     pass


# @login_required
# def mensalistas_detail(request):
#     pass


# @login_required
# def mensalistas_edit(request):
#     pass


# @login_required
# def mensalistas_delete(request):
#     pass
