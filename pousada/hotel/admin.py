from django.contrib import admin
from .models import Pessoa, Quarto, Mensalista, MovRotativo


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cidade', 'telefone')
    search_fields = ('nome', 'cpf', 'cidade', 'telefone')


@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('padrao', 'numero', 'hospede', 'cor')


@admin.register(Mensalista)
class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('quarto', 'inicio', 'valor_mes')


@admin.register(MovRotativo)
class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'quarto', 'pago')
