from django.urls import path
from .views import *


app_name = 'core'


urlpatterns = [
    path('', home, name='core_home'),

    path('pesso/', pesso_view, name='core_pessoas'),
    path('pesso/add/', pesso_add, name='core_pessoas_add'),
    path('pesso/<int:pk>/', pesso_detail, name='core_pessoas_detail'),
    # path('pesso/<int:pk>/<int:cmd>/', pesso_view, name='core_pessoas'),

    # url quart onde lista todas quartos cadastradas
    # quart +id + comando mostra determinada quarto cadastrada e determinado
    # comando, update ou delete
    path('quart/', quart_view, name='core_quartos'),
    path('quart/<int:pk>/', quart_view, name='core_quartos'),
    path('quart/<int:pk>/<int:cmd>/', quart_view, name='core_quartos'),

    # url rota onde lista todas rotas cadastradas
    # rota +id + comando mostra determinada rota cadastrada e determinado
    # comando, update ou delete
    path('rota/', rotati_view, name='core_rotativos'),
    path('rota/<int:pk>/', rotati_view, name='core_rotativos'),
    path(
        'rota/<int:pk>/<int:cmd>/',
        rotati_view,
        name='core_rotativos'
    ),

    # url men onde lista todos mensalista cadastradas
    # men +id + comando mostra determinada mensalista cadastrada e determinado
    # comando, update ou delete
    path('men/', mensalista_view, name='core_mensalista'),
    path('men/<int:pk>/', mensalista_view, name='core_mensalista'),
    path(
        'men/<int:pk>/<int:cmd>/',
        mensalista_view,
        name='core_mensalista'
    ),

    # url movmensal onde lista todas movmensal cadastradas
    # movmensal +id + comando mostra determinada movmensal cadastrada e
    # determinado comando, update ou delete
    path('movmensal/', movmensal_view, name='core_movmensalista'),
    path('movmensal/<int:pk>/', movmensal_view, name='core_movmensalista'),
    path(
        'movmensal/<int:pk>/<int:cmd>/',
        movmensal_view,
        name='core_movmensalista'
    ),

]
