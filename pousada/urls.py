from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import urls

#urls que transitam de index para outra
urlpatterns = [
    url(r'home/', include('website.urls')),
    url(r'sistema/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
