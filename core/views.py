from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .models import Pessoa, Quarto, MovRotativo, Mensalista, MovMensalista

# importa todos os itens que estao dentro de forms.py.
# caso queira que importa apenas especifico Ex1(from .forms import Pessoa)
from .forms import *


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


@login_required
def pesso_view(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {
        'pessoas': pessoas,
        'form': form,
    }
    return render(request, 'core/pessoas.html', data)


@login_required
def pesso_add(request):
    form = PessoaForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(resolve_url('core:core_pessoas'))


# Função que faz uma requisição pelo id,comando, pegando o objeto pessoa,
# Caso o id e comando estiver 0 o update sera false e entao o form sera null
# Caso o comando seja diferente de 0 habilita o update para true buscando o objeto pessoa pelo PrimaryKey ID
# E entao o form faz uma requisiçao metodo POST caso seja null ele instacia o form metodo post
# Se o Form estiver valido Pessoa salvo com sucesso
# Caso comando estiver 0 vai fazer uma requisiçaõ POST para preenche formulario validar o form e adicionar a pessoa
# O se instanciar o objeto pessoa pelo primarykey id intancia o objeto
# pessoaform retornando id e comando pessoa removida


@login_required()
def pesso_view_old(request, id=0, cmd=0):
    pessoas = Pessoa.objects.all()
    msg = ''
    cmd = int(cmd)
    id = int(id)

    print('******', id, cmd)

    is_update = False
    form = None
    if cmd == 1:
        is_update = True
        m = Pessoa.objects.get(pk=id)
        form = PessoaForm(request.POST or None, instance=m)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Pessoa salvo com sucesso'
    elif cmd == 0:
        form = PessoaForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Pessoa adicionado com sucesso'
    else:
        m = Pessoa.objects.get(pk=id)
        m.delete()
        form = PessoaForm(request.POST or None)
        cmd = 0
        id = 0
        msg = 'Pessoa removido com sucesso'

    data = {
        'pessoas': pessoas,
        'form': form,
        'update': is_update,
        'message': msg,
        'id': id,
        'cmd': cmd
    }
    return render(request, 'core/pessoas.html', data)

# Função que faz uma requisição pelo id,comando, pegando o objeto quarto,
# Caso o id e comando estiver 0 o update sera false e entao o form sera null
# Caso o comando seja diferente de 0 habilita o update para true buscando o objeto quarto pelo PrimaryKey ID
# E entao o form faz uma requisiçao metodo POST caso seja null ele instacia o form metodo post
# Se o Form estiver valido quarto salvo com sucesso
# Caso comando estiver 0 vai fazer uma requisiçaõ POST para preenche formulario validar o form e adicionar a quarto
# O se instanciar o objeto quarto pelo primarykey id intancia o objeto
# quartoform retornando id e comando quarto removida


@login_required()
def quart_view(request, id=0, cmd=0):
    quartos = Quarto.objects.all()
    msg = ''
    cmd = int(cmd)
    id = int(id)

    print('******', id, cmd)

    is_update = False
    form = None
    if cmd == 1:
        is_update = True
        m = Quarto.objects.get(pk=id)
        form = QuartoForm(request.POST or None, instance=m)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Quarto salvo com sucesso'
    elif cmd == 0:
        form = QuartoForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Quarto adicionado com sucesso'
    else:
        m = Quarto.objects.get(pk=id)
        m.delete()
        form = QuartoForm(request.POST or None)
        cmd = 0
        id = 0
        msg = 'Quarto removido com sucesso'

    data = {'quartos': quartos, 'form': form,
            'update':  is_update, 'message': msg, 'id': id, 'cmd': cmd}
    return render(request, 'core/quartos.html', data)

# Função que faz uma requisição pelo id,comando, pegando o objeto MovRotativo,
# Caso o id e comando estiver 0 o update sera false e entao o form sera null
# Caso o comando seja diferente de 0 habilita o update para true buscando o objeto MovRotativo pelo PrimaryKey ID
# E entao o form faz uma requisiçao metodo POST caso seja null ele instacia o form metodo post
# Se o Form estiver valido MovRotativo salvo com sucesso
# Caso comando estiver 0 vai fazer uma requisiçaõ POST para preenche formulario validar o form e adicionar a MovRotativo
# O se instanciar o objeto MovRotativo pelo primarykey id intancia o
# objeto MovRotativoform retornando id e comando MovRotativo removida


@login_required()
def rotati_view(request, id=0, cmd=0):
    mov_rot = MovRotativo.objects.all()
    msg = ''
    cmd = int(cmd)
    id = int(id)

    print('******', id, cmd)

    is_update = False
    form = None
    if cmd == 1:
        is_update = True
        m = MovRotativo.objects.get(pk=id)
        form = MovRotativoForm(request.POST or None, instance=m)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Rotativo salvo com sucesso'
    elif cmd == 0:
        form = MovRotativoForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Rotativo adicionado com sucesso'
    else:
        m = MovRotativo.objects.get(pk=id)
        m.delete()
        form = MovRotativoForm(request.POST or None)
        cmd = 0
        id = 0
        msg = 'Rotativo removido com sucesso'

    data = {'mov_rot': mov_rot, 'form': form,
            'update':  is_update, 'message': msg, 'id': id, 'cmd': cmd}
    return render(request, 'core/rotativos.html', data)

# Função que faz uma requisição pelo id,comando, pegando o objeto Mensalista,
# Caso o id e comando estiver 0 o update sera false e entao o form sera null
# Caso o comando seja diferente de 0 habilita o update para true buscando o objeto Mensalista pelo PrimaryKey ID
# E entao o form faz uma requisiçao metodo POST caso seja null ele instacia o form metodo post
# Se o Form estiver valido Mensalista salvo com sucesso
# Caso comando estiver 0 vai fazer uma requisiçaõ POST para preenche formulario validar o form e adicionar a Mensalista
# O se instanciar o objeto Mensalista pelo primarykey id intancia o objeto
# Mensalistaform retornando id e comando Mensalista removida


@login_required()
def mensalista_view(request, id=0, cmd=0):
    mensalistas = Mensalista.objects.all()
    msg = ''
    cmd = int(cmd)
    id = int(id)

    print('******', id, cmd)

    is_update = False
    form = None
    if cmd == 1:
        is_update = True
        m = Mensalista.objects.get(pk=id)
        form = MensalistaForm(request.POST or None, instance=m)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Mensalista salvo com sucesso'
    elif cmd == 0:
        form = MensalistaForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Mensalista adicionado com sucesso'
    else:
        m = Mensalista.objects.get(pk=id)
        m.delete()
        form = MensalistaForm(request.POST or None)
        cmd = 0
        id = 0
        msg = 'Mensalista removido com sucesso'

    data = {'mensalistas': mensalistas, 'form': form,
            'update':  is_update, 'message': msg, 'id': id, 'cmd': cmd}
    return render(request, 'core/mensalista.html', data)

# Função que faz uma requisição pelo id,comando, pegando o objeto MovMensalista,
# Caso o id e comando estiver 0 o update sera false e entao o form sera null
# Caso o comando seja diferente de 0 habilita o update para true buscando o objeto MovMensalista pelo PrimaryKey ID
# E entao o form faz uma requisiçao metodo POST caso seja null ele instacia o form metodo post
# Se o Form estiver valido MovMensalista salvo com sucesso
# Caso comando estiver 0 vai fazer uma requisiçaõ POST para preenche formulario validar o form e adicionar a MovMensalista
# O se instanciar o objeto MovMensalista pelo primarykey id intancia o
# objeto MovMensalistaform retornando id e comando MovMensalista removida


@login_required()
def movmensal_view(request, id=0, cmd=0):
    mov_mensal = MovMensalista.objects.all()
    msg = ''
    cmd = int(cmd)
    id = int(id)

    print('******', id, cmd)

    is_update = False
    form = None
    if cmd == 1:
        is_update = True
        m = MovMensalista.objects.get(pk=id)
        form = MovMensalistaForm(request.POST or None, instance=m)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Mensalista salvo com sucesso'
    elif cmd == 0:
        form = MovMensalistaForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                msg = 'Mensalista adicionado com sucesso'
    else:
        m = MovMensalista.objects.get(pk=id)
        m.delete()
        form = MovMensalistaForm(request.POST or None)
        cmd = 0
        id = 0
        msg = 'Mensalista removido com sucesso'

    data = {'mov_mensal': mov_mensal, 'form': form,
            'update':  is_update, 'message': msg, 'id': id, 'cmd': cmd}
    return render(request, 'core/movmensalista.html', data)
