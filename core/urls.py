from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$',home, name='core_home'),

    #url pesso onde lista todas pessoas cadastradas
    #pesso +id + comando mostra determinada pessoa cadastrada e determinado comando, update ou delete
    url(r'^pesso/$', pesso_view, name='core_pessoas'),
    url(r'^pesso/(?P<id>\d+)/$', pesso_view, name='core_pessoas'),
    url(r'^pesso/(?P<id>\d+)/(?P<cmd>\d+)/$', pesso_view, name='core_pessoas'),

    #url quart onde lista todas quartos cadastradas
    #quart +id + comando mostra determinada quarto cadastrada e determinado comando, update ou delete
    url(r'^quart/$', quart_view, name='core_quartos'),
    url(r'^quart/(?P<id>\d+)/$', quart_view, name='core_quartos'),
    url(r'^quart/(?P<id>\d+)/(?P<cmd>\d+)/$', quart_view, name='core_quartos'),

    #url rota onde lista todas rotas cadastradas
    #rota +id + comando mostra determinada rota cadastrada e determinado comando, update ou delete
    url(r'^rota/$', rotati_view, name='core_rotativos'),
    url(r'^rota/(?P<id>\d+)/$', rotati_view, name='core_rotativos'),
    url(r'^rota/(?P<id>\d+)/(?P<cmd>\d+)/$', rotati_view, name='core_rotativos'),

    #url men onde lista todos mensalista cadastradas
    #men +id + comando mostra determinada mensalista cadastrada e determinado comando, update ou delete
    url(r'^men/$', mensalista_view, name='core_mensalista'),
    url(r'^men/(?P<id>\d+)/$', mensalista_view, name='core_mensalista'),
    url(r'^men/(?P<id>\d+)/(?P<cmd>\d+)/$', mensalista_view, name='core_mensalista'),

    #url movmensal onde lista todas movmensal cadastradas
    #movmensal +id + comando mostra determinada movmensal cadastrada e determinado comando, update ou delete
    url(r'^movmensal/$', movmensal_view, name='core_movmensalista'),
    url(r'^movmensal/(?P<id>\d+)/$', movmensal_view, name='core_movmensalista'),
    url(r'^movmensal/(?P<id>\d+)/(?P<cmd>\d+)/$', movmensal_view, name='core_movmensalista'),

]