from django.urls import path

from meuSite import views

app_name = 'estetica'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('facial', views.facial, name='facial'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('<int:servico_id>/<slug:tag_servico>', views.servico, name='servico'),
    path('servicos/cadastro', views.cadastro, name='cadastro'),
    path('servicos', views.servico_listar, name='servico_listar'),
    path('servicos/editar/<int:id_servico>/', views.servico_editar, name='servico_editar'),
    path('servicos/deletado/<int:servico_id>', views.servico_remover, name='servico_remover'),
    path('servicos/pesquisa', views.pesquisa, name='pesquisa'),
    path('pacotes', views.pacotes, name='pacotes'),
    path('adicionar_ao_carrinho', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),

]
