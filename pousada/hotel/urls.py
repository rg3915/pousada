from django.urls import include, path
from pousada.hotel import views as v


app_name = 'hotel'

dashboard_patterns = [
    path('dashboard/', v.dashboard, name='dashboard'),
]

pessoas_patterns = [
    path('pessoas/', v.pessoas, name='pessoas'),
]

quartos_patterns = [
    path('quartos/', v.quartos, name='quartos'),
]

rotativos_patterns = [
    path('rotativos/', v.rotativos, name='rotativos'),
]

mensalistas_patterns = [
    path('mensalistas/', v.mensalistas, name='mensalistas'),
    # path('mov_mensalistas/', v.mov_mensalistas, name='mov_mensalistas'),
]


urlpatterns = [
    path('', include(dashboard_patterns)),
    path('pessoas/', include(pessoas_patterns)),
    path('quartos/', include(quartos_patterns)),
    path('rotativos/', include(rotativos_patterns)),
    path('mensalistas/', include(mensalistas_patterns)),
]
