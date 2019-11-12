from django.urls import include, path
from pousada.hotel import views as v


app_name = 'hotel'

dashboard_patterns = [
    path('dashboard/', v.dashboard, name='dashboard'),
]

pessoas_patterns = [
    path('pessoas/', v.pessoas, name='pessoas'),
    path('pessoas/add/', v.pessoas_add, name='pessoas_add'),
    path('pessoas/<int:pk>/edit', v.pessoas_edit, name='pessoas_edit'),
    path('pessoas/<int:pk>/delete', v.pessoas_delete, name='pessoas_delete'),
]

quartos_patterns = [
    path('quartos/', v.quartos, name='quartos'),
    path('quartos/add/', v.quartos_add, name='quartos_add'),
    path('quartos/<int:pk>/edit', v.quartos_edit, name='quartos_edit'),
    path('quartos/<int:pk>/delete', v.quartos_delete, name='quartos_delete'),
]

pre_reserva_patterns = [
    path('', v.pre_reserva, name='pre_reserva'),
    path(
        'pessoas/add/',
        v.pre_reserva_pessoa_add,
        name='pre_reserva_pessoas_add'
    ),
    path(
        'reserva/add/',
        v.pre_reserva_reserva_add,
        name='pre_reserva_reserva_add'
    ),
    path('checkout/<int:pk>/', v.checkout, name='checkout'),
    path('<int:pk>/json/', v.pre_reserva_json, name='pre_reserva_json'),
    # path('checkout/<int:pk>/final/', v.checkout_final, name='checkout_final'),
]

reserva_patterns = [
    path('reserva/', v.reserva, name='reserva'),
    path('reserva/add/', v.ReservaAdd.as_view(), name='reserva_add'),
    # path('reserva/<int:pk>/', v.reserva_detail, name='reserva_detail'),
    # path('reserva/<int:pk>/edit', v.reserva_edit, name='reserva_edit'),
    # path('reserva/<int:pk>/delete', v.reserva_delete, name='reserva_delete'),
]


urlpatterns = [
    path('', include(dashboard_patterns)),
    path('pessoas/', include(pessoas_patterns)),
    path('quartos/', include(quartos_patterns)),
    path('reserva/', include(reserva_patterns)),
    path('pre_reserva/', include(pre_reserva_patterns)),
]
