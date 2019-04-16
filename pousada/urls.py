from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('website.urls')),
    path('sistema/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
