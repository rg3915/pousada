from django.conf.urls import url, include
from django.urls import path
from .views import home, contato, servicos


#urls que transitam de um template para o outro dentro de website
urlpatterns = [
    url(r'^home$', home, name='website_home'),
    url(r'^contato$', contato, name='website_contato'),
    path('servicos', servicos, name='website_servicos'),
]