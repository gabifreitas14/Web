from django.urls import path

from meuSite import views

app_name = 'estetica'

urlpatterns = [
    path('', views.index, name='index'),
    path('facial', views.facial, name='facial'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
    path('servico/cadastro', views.cadastro, name='cadastro'),
    path('servico', views.servico_listar, name='servico_listar'),
    path('servico/editar/<int:id_servico>/', views.servico_editar, name='servico_editar'),
    path('servico/deletado/<int:servico_id>', views.servico_remover, name='servico_remover'),

]
