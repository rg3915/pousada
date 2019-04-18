from django.urls import path
from .views import home, contato, servicos


app_name = 'hotel'


urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('servicos/', servicos, name='servicos'),
]
