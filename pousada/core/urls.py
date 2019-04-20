from django.urls import path
from pousada.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.home, name='home'),
    path('servicos/', v.servicos, name='servicos'),
    path('contato/', v.contato, name='contato'),
    path('contato/add/', v.contato_add, name='contato_add'),
]
