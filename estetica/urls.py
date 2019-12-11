from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from estetica import views

urlpatterns = [
    path('', include('meuSite.urls')),
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),

]
urlpatterns += staticfiles_urlpatterns()
