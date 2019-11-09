from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.urls import reverse
from django.utils import timezone
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


def pre_reserva_pessoa_add(request):
    form = PessoaForm(request.POST or None)
    template_name = 'hotel/pessoas_add.html'
    if request.method == 'POST':
        quarto_pk = request.session['quarto']
        quarto = Quarto.objects.get(pk=quarto_pk)
        # Salvando os dados da Pessoa.
        if form.is_valid():
            obj = form.save()  # salva a Pessoa
            # Fazer a reserva do Quarto com a pessoa cadatrada.
            request.session['pessoa'] = obj.pk  # obj.pk é o pk da Pessoa.
            url = 'hotel:pre_reserva_reserva_add'
            return HttpResponseRedirect(resolve_url(url))
    else:
        # Para pegar dados que vem junto com a interrogação na url,
        # usamos request.GET.get('chave').
        response = request.GET.get('quarto')
        # O response vem com o pk do quarto.
        quarto = Quarto.objects.get(pk=response)
        request.session['quarto'] = response
        request.session['valor_diaria'] = float(quarto.valor_diaria)
    context = {'form': form, 'quarto': quarto}
    return render(request, template_name, context)


def pre_reserva_reserva_add(request):
    form = ReservaForm(request.POST or None)
    template_name = 'hotel/reservas_add.html'
    response_pessoa = None
    response_quarto = None
    response_valor_diaria = None

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(resolve_url('hotel:reserva'))
    else:
        response_pessoa = request.session['pessoa']
        response_quarto = request.session['quarto']
        response_valor_diaria = request.session['valor_diaria']

    context = {
        'form': form,
        'quarto': response_quarto,
        'pessoa': response_pessoa,
        'valor_diaria': response_valor_diaria,
    }
    return render(request, template_name, context)


def checkout(request, pk):
    reserva = Reserva.objects.get(pk=pk)
    reserva.checkout = timezone.now()
    reserva.save()

    kw = {'pk': pk}
    url = 'hotel:checkout_final'
    return HttpResponseRedirect(reverse(url, kwargs=kw))


def checkout_final(request, pk):
    # O pk é o pk da reserva.
    reserva = Reserva.objects.get(pk=pk)
    dias_hospedado = (reserva.checkout - reserva.checkin).days
    saldo_devedor = dias_hospedado * reserva.quarto.valor_diaria

    if request.method == 'POST':
        # valor_diaria seria o valor total (final) da reserva,
        # após checkout.
        reserva.valor_diaria = saldo_devedor
        pago = request.POST.get('pago')
        if pago == 'on':
            reserva.pago = True
        else:
            reserva.pago = False
        reserva.save()
        return HttpResponseRedirect(resolve_url('hotel:reserva'))
    else:
        context = {'saldo_devedor': saldo_devedor}

    template_name = 'hotel/checkout_final.html'
    return render(request, template_name, context)


@login_required
def quartos(request):
    quartos = Quarto.objects.all()
    template_name = 'hotel/quartos.html'
    context = {'quartos': quartos}
    return render(request, template_name, context)


# @login_required
# def quartos_add(request):
#     form = QuartoForm(request.POST)
#     template_name = 'hotel/quartos_add.html'
#     context = {'form': form}
#     return render(request, template_name, context)

class QuartosAdd(CreateView):
    model = Quarto
    form_class = QuartoForm
    template_name = 'hotel/quartos_add.html'


# @login_required
# def quartos_detail(request):
#     pass


# @login_required
# def quartos_edit(request):
#     pass


# @login_required
# def quartos_delete(request):
#     pass


# @login_required
def pre_reserva(request):
    quartos = Quarto.objects.all()
    context = {'object_list': quartos}
    template_name = 'hotel/pre_reserva.html'
    return render(request, template_name, context)


@login_required
def reserva(request):
    object_list = Reserva.objects.all()
    template_name = 'hotel/reservas.html'
    context = {'object_list': object_list}
    return render(request, template_name, context)


class ReservaAdd(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'hotel/reservas_add.html'


# @login_required
# def reserva_detail(request):
#     pass


# @login_required
# def reserva_edit(request):
#     pass


# @login_required
# def reserva_delete(request):
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
