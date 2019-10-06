from django.urls import path

from meuSite import views

app_name = 'estetica'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.facial, name='facial'),
    path('', views.contato, name='contato'),
    path('', views.sobre, name='sobre'),
]
