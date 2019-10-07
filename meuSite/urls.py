from django.urls import path

from meuSite import views

app_name = 'estetica'

urlpatterns = [
    path('', views.index, name='index'),
    path('facial', views.facial, name='facial'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
]
