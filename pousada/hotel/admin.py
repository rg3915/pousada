from django.contrib import admin
from .models import Pessoa, Padrao, Quarto, Mensalista, MovRotativo


@admin.register(Padrao)
class PadraoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cidade', 'telefone')
    search_fields = ('nome', 'cpf', 'cidade', 'telefone')


@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('padrao', 'numero',)


@admin.register(Mensalista)
class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('quarto', 'inicio', 'valor_mes')


@admin.register(MovRotativo)
class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'quarto', 'pago')
