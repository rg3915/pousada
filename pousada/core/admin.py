from django.contrib import admin
from .models import Padrao, Quarto, Pessoa, Parametros, MovRotativo, Mensalista, MovMensalista

# class MovRotativoAdmin(admin.ModelAdmin):
#     list_display = ('checkin', 'checkout', 'valor_hora', 'pago', 'total', 'horas_total', 'quarto')

#     def quarto(self, obj):
#         return obj.quarto

# class MovMensalistaAdmin(admin.ModelAdmin):
#     list_display = ('mensalista', 'dt_pgto')


# admin.site.register(Padrao)
# admin.site.register(Quarto)
# admin.site.register(Pessoa)
# admin.site.register(Parametros)
# admin.site.register(Mensalista)
# admin.site.register(MovMensalista)
# admin.site.register(MovRotativo,MovRotativoAdmin)
