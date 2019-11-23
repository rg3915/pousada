from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from .models import Pessoa, Quarto, Reserva
from .forms import PessoaForm, QuartoForm, ReservaForm


@login_required
def dashboard(request):
    clientes = Pessoa.objects.all()
    reservas = Reserva.objects.all()
    context = {
        'clientes': clientes,
        'reservas': reservas,
    }
    return render(request, 'hotel/dashboard.html', context)


@login_required
def pessoas(request):
    template_name = 'hotel/pessoas.html'
    pessoas = Pessoa.objects.all()
    form = PessoaForm()

    pk = request.GET.get('pk')
    if pk:
        pessoa = Pessoa.objects.get(pk=pk)
        form = PessoaForm(request.POST or None, instance=pessoa)

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
    return render(request, template_name, data)


@login_required
def pessoas_edit(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('hotel:pessoas'))


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
def pre_reserva(request):
    quartos = Quarto.objects.all()
    template_name = 'hotel/pre_reserva.html'
    form = PessoaForm()
    form_reserva = ReservaForm()

    # Search
    search = request.GET.get('search')
    if search:
        quartos = quartos.filter(
            Q(titulo__icontains=search,) |
            Q(padrao__nome__icontains=search,)
        )

    context = {
        'object_list': quartos,
        'form': form,
        'form_reserva': form_reserva,
    }
    return render(request, template_name, context)


def pre_reserva_json(request, pk):
    reserva = Reserva.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in reserva]
    return JsonResponse({'data': data})


def pre_reserva_pessoa_add(request):
    form = PessoaForm(request.POST or None)
    if request.method == 'POST' and request.is_ajax():
        # Salvando os dados da Pessoa.
        if form.is_valid():
            obj = form.save()  # salva a Pessoa
            response = {'pessoa': obj.pk}
            return JsonResponse(response)


def convert_date(date):
    if date:
        return datetime.strptime(date, '%d/%m/%Y')


def pre_reserva_reserva_add(request):
    form = ReservaForm(request.POST or None)
    if request.method == 'POST' and request.is_ajax():
        quarto_pk = request.POST.get('quarto_pk')
        pessoa_pk = request.POST.get('pessoa_pk')
        valor_diaria = request.POST.get('valor_diaria')
        checkin = request.POST.get('checkin')
        pre_checkout = request.POST.get('pre_checkout')
        forma_pagto = request.POST.get('forma_pagto')

        if form.is_valid():
            quarto = Quarto.objects.get(pk=quarto_pk)
            nome_cliente = Pessoa.objects.get(pk=pessoa_pk)
            obj = Reserva(
                quarto=quarto,
                nome_cliente=nome_cliente,
                valor_diaria=valor_diaria,
                checkin=convert_date(checkin),
                pre_checkout=convert_date(pre_checkout),
                forma_pagto=forma_pagto,
            )
            obj.save()
            response = {'response': 'OK'}
            return JsonResponse(response)


@csrf_exempt
def checkout(request, pk):
    if request.method == 'POST' and request.is_ajax():
        reserva = Reserva.objects.get(pk=pk)
        reserva.checkout = timezone.now()
        reserva.save()
        return JsonResponse({'data': 'OK'})


@login_required
def quartos(request):
    quartos = Quarto.objects.all()
    template_name = 'hotel/quartos.html'
    form = QuartoForm()

    pk = request.GET.get('pk')
    if pk:
        quarto = Quarto.objects.get(pk=pk)
        form = QuartoForm(request.POST or None, instance=quarto)

    # Search
    search = request.GET.get('search')
    if search:
        quartos = quartos.filter(
            Q(titulo__icontains=search,) |
            Q(padrao__nome__icontains=search,)
        )

    context = {
        'quartos': quartos,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def quartos_add(request):
    form = QuartoForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(resolve_url('hotel:quartos'))


@login_required
def quartos_edit(request, pk):
    quarto = Quarto.objects.get(pk=pk)
    form = QuartoForm(request.POST or None, instance=quarto)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('hotel:quartos'))


@login_required
def quartos_delete(request, pk):
    quarto = Quarto.objects.get(pk=pk)
    quarto.delete()
    return HttpResponseRedirect(resolve_url('hotel:quartos'))


@login_required
def reserva(request):
    object_list = Reserva.objects.all()
    template_name = 'hotel/reservas.html'

    # Search
    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(quarto__titulo__icontains=search,) |
            Q(quarto__padrao__nome__icontains=search,) |
            Q(nome_cliente__nome__icontains=search,)
        )

    context = {'object_list': object_list}
    return render(request, template_name, context)


class ReservaAdd(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'hotel/reservas_add.html'
