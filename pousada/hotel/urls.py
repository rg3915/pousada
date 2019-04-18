from django.urls import path
from pousada.hotel import views as v


app_name = 'hotel'


urlpatterns = [
    path('dashboard', v.dashboard, name='dashboard'),
]
