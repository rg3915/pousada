from django.urls import include, path
from pousada.hotel import views as v


app_name = 'hotel'

dashboard_patterns = [
    path('dashboard/', v.dashboard, name='dashboard'),
]

pessoas_patterns = [
    path('pessoas/', v.pessoas, name='pessoas'),
    path('pessoas/add/', v.pessoas_add, name='pessoas_add'),
    path('pessoas/<int:pk>/', v.pessoas_detail, name='pessoas_detail'),
    path('pessoas/<int:pk>/edit', v.pessoas_edit, name='pessoas_edit'),
    path('pessoas/<int:pk>/delete', v.pessoas_delete, name='pessoas_delete'),
]

quartos_patterns = [
    path('quartos/', v.quartos, name='quartos'),
    path('quartos/add/', v.QuartosAdd.as_view(), name='quartos_add'),
    # path('quartos/<int:pk>/', v.quartos_detail, name='quartos_detail'),
    # path('quartos/<int:pk>/edit', v.quartos_edit, name='quartos_edit'),
    # path('quartos/<int:pk>/delete', v.quartos_delete, name='quartos_delete'),
]

reserva_patterns = [
    path('reserva/', v.reserva, name='reserva'),
    path('reserva/add/', v.ReservaAdd.as_view(), name='reserva_add'),
    # path('reserva/<int:pk>/', v.reserva_detail, name='reserva_detail'),
    # path('reserva/<int:pk>/edit', v.reserva_edit, name='reserva_edit'),
    # path('reserva/<int:pk>/delete', v.reserva_delete, name='reserva_delete'),
]

mensalistas_patterns = [
    path('mensalistas/', v.mensalistas, name='mensalistas'),
    # path('mensalistas/add/', v.mensalistas_add, name='mensalistas_add'),
    # path('mensalistas/<int:pk>/', v.mensalistas_detail, name='mensalistas_detail'),
    # path('mensalistas/<int:pk>/edit', v.mensalistas_edit, name='mensalistas_edit'),
    # path('mensalistas/<int:pk>/delete', v.mensalistas_delete, name='mensalistas_delete'),
]


urlpatterns = [
    path('', include(dashboard_patterns)),
    path('pessoas/', include(pessoas_patterns)),
    path('quartos/', include(quartos_patterns)),
    path('reserva/', include(reserva_patterns)),
    path('mensalistas/', include(mensalistas_patterns)),
]
