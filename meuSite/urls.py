from django.urls import path

from meuSite import views

app_name = 'estetica'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('facial', views.facial, name='facial'),
    path('corporal', views.corporal, name='corporal'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
    path('carrinho', views.exibe_carrinho, name='carrinho'),
    path('remove_servico_carrinho/', views.remove_servico_carrinho, name='remove_servico_carrinho'),
    path('atualiza_qtd_carrinho/', views.atualiza_qtd_carrinho, name='atualiza_qtd_carrinho'),
    path('<int:servico_id>/<slug:tag_servico>', views.servico, name='servico'),
    path('servicos/cadastro', views.cadastro, name='cadastro'),
    path('servicos', views.servico_listar, name='servico_listar'),
    path('servicos/editar/<int:id_servico>/', views.servico_editar, name='servico_editar'),
    path('servicos/deletado/<int:servico_id>', views.servico_remover, name='servico_remover'),
    path('servicos/pesquisa', views.pesquisa, name='pesquisa'),
    path('pacotes', views.pacotes, name='pacotes'),
    path('adicionar_ao_carrinho', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),

]
