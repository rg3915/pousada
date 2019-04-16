from django.urls import path
from .views import home, contato, servicos


urlpatterns = [
    path('home/', home, name='website_home'),
    path('contato/', contato, name='website_contato'),
    path('servicos/', servicos, name='website_servicos'),
]
