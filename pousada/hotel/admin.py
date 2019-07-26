from django.contrib import admin
from .models import Pessoa, Padrao, Quarto, Mensalista, Reserva


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
    list_display = ('__str__', 'padrao', 'valor_diaria',)


@admin.register(Mensalista)
class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('quarto', 'inicio', 'valor_mes')


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'checkin', 'checkout', 'quarto', 'pago')
