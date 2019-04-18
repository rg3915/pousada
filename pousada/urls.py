from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('pousada.core.urls')),
    path('hotel/', include('pousada.hotel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
