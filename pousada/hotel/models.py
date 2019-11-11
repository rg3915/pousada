from django.shortcuts import resolve_url
from django.db import models
import math


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField('CPF', max_length=14)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    endereco = models.CharField(
        'endereço', max_length=200, null=True, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Padrao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Quarto(models.Model):
    titulo = models.CharField('título', max_length=200)
    padrao = models.ForeignKey(
        Padrao,
        verbose_name='padrão',
        on_delete=models.CASCADE
    )
    numero = models.IntegerField('número')
    valor_diaria = models.DecimalField(
        'valor diária', max_digits=6, decimal_places=2)
    observacoes = models.TextField('observações', null=True, blank=True)

    class Meta:
        ordering = ('numero',)
        verbose_name = 'quarto'
        verbose_name_plural = 'quartos'

    def __str__(self):
        return '{} - {}'.format(self.numero, self.titulo)

    def get_absolute_url(self):
        return resolve_url('hotel:quartos')  # , pk=self.pk

    def reservado(self):
        # Verifica se o quarto está reservado ou não.
        esta_reservado = Reserva.objects.filter(
            quarto=self, checkout__isnull=True).first()
        if esta_reservado:
            return True
        return False

    def reserva(self):
        # Se o quarto estiver reservado, então
        # retorna os quartos reservados.
        reserva = Reserva.objects.filter(
            quarto=self, checkout__isnull=True).first()
        if reserva:
            return reserva


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return 'Parametros Gerais'


FORMA_PAGTO = (
    ('di', 'Dinheiro'),
    ('de', 'Débito'),
    ('cr', 'Crédito'),
)


class Reserva(models.Model):
    nome_cliente = models.ForeignKey(
        Pessoa,
        verbose_name='cliente',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, blank=True)
    valor_diaria = models.DecimalField(
        'valor diária',
        max_digits=6,
        decimal_places=2,
        help_text='Valor do quarto reservado.'
    )
    checkin = models.DateTimeField('Entrada', auto_now=False)
    pre_checkout = models.DateTimeField('Previsão de Saída', auto_now=False)
    checkout = models.DateTimeField(
        'Saída',
        auto_now=False,
        null=True,
        blank=True
    )
    forma_pagto = models.CharField(
        'forma de pagto',
        max_length=2,
        choices=FORMA_PAGTO,
        default='de',
    )
    pago = models.BooleanField(default=False)
    created = models.TimeField(auto_now=True)

    class Meta:
        # ordering = ('nome_cliente',)
        ordering = ('-pk',)
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'

    def __str__(self):
        return str(self.quarto.numero)

    def get_absolute_url(self):
        return resolve_url('hotel:reserva')  # , pk=self.pk

    def horas_total(self):
        return math.ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
        return self.valor_hora * self.horas_total()


class Mensalista(models.Model):
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.quarto) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)
