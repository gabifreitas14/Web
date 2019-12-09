from django.contrib import admin
from django.urls import path, include

from estetica import views

urlpatterns = [
    path('', include('meuSite.urls')),
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),

]
