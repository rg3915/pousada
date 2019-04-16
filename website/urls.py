from django.urls import path
from .views import home, contato, servicos


app_name = 'website'


urlpatterns = [
    path('', home, name='website_home'),
    path('contato/', contato, name='website_contato'),
    path('servicos/', servicos, name='website_servicos'),
]
