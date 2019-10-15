from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from meuSite.forms import ServicoForm, RemoveServicoForm
from .models import FotoCarousel, DestaqueServico, Servico


def index(request):
    fotos_carousel = FotoCarousel.objects.all()
    destaques = DestaqueServico.objects.all().order_by('ordem')

    return render(request, 'index.html', {'fotos_carousel': fotos_carousel, 'destaques': destaques})


def facial(request):
    procedimentos_faciais = Servico.objects.filter(tipo__nome__contains='facial')
    return render(request, 'facial.html', {'servicos': procedimentos_faciais})


def contato(request):
    return render(request, 'contato.html')


def sobre(request):
    return render(request, 'sobre.html')


def pesquisa(request):
    if request.method == 'GET':
        palavra = request.GET.get('input-pesquisa')
        lista_servicos = Servico.objects.filter(nome__contains=palavra)
        if lista_servicos.count() == 0:
            messages.add_message(request, messages.ERROR, 'Nada foi encontrado.')
        else:
            messages.add_message(request, messages.INFO, 'Pesquisa por "'+palavra+'" realizada com sucesso!')
        return render(request, 'servico_listar.html', {'servicos': lista_servicos})
    return redirect('estetica:servico_listar')

def servico_listar(request):
    servicos = Servico.objects.all().order_by('nome')
    return render(request, 'servico_listar.html', {'servicos': servicos})


def servico_editar(request, id_servico):
    servico = get_object_or_404(Servico, pk=id_servico)
    servico_form = ServicoForm(instance=servico)
    servico_form.fields['servico_id'].initial = id_servico
    return render(request, 'servico_editar.html', {'form': servico_form})


def servico_remover(request, servico_id):
    #   form_remove_produto = RemoveProdutoForm(request.POST)
    #   if form_remove_produto.is_valid:
    # produto_id = form_remove_produto.cleaned_data['produto_id']
    servico = get_object_or_404(Servico, id=servico_id)
    form = RemoveServicoForm(initial={'servico_id': servico_id})
    servico.delete()
    messages.add_message(request, messages.INFO, 'Serviço removido com sucesso.')
    return redirect('estetica:servico_listar')

    #   else:
    #      raise ValueError('Ocorreu um erro inesperado ao tentar remover um produto.')


def cadastro(request):
    if request.POST:
        servico_id = request.POST.get('servico_id')
        if servico_id:
            servico = get_object_or_404(Servico, pk=servico_id)
            servico_form = ServicoForm(request.POST, instance=servico)
        else:
            servico_form = ServicoForm(request.POST)
        if servico_form.is_valid():
            servico = servico_form.save()
            if servico_id:
                messages.add_message(request, messages.INFO, 'Serviço alterado com sucesso!')
            else:
                messages.add_message(request, messages.INFO, 'Serviço cadastrado com sucesso!')
            return redirect('estetica:servico_listar')
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        servico_form = ServicoForm()
    return render(request, 'servico_editar.html', {'form': servico_form})
