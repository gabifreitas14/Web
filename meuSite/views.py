from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from meuSite.forms import ServicoForm, RemoveServicoForm, PesquisaServicoForm
from .models import FotoCarousel, DestaqueServico, Servico
from django.core.paginator import Paginator


def index(request):
    fotos_carousel = FotoCarousel.objects.all()
    destaques = DestaqueServico.objects.all().order_by('ordem')

    return render(request, 'index.html', {'fotos_carousel': fotos_carousel, 'destaques': destaques})


def facial(request):
    procedimentos_faciais = Servico.objects.filter(tipo__nome__contains='facial')
    return render(request, 'facial.html', {'servicos': procedimentos_faciais})


def contato(request):
    return render(request, 'contato.html')


def login(request):
    return render(request, 'registration/login.html')


def sobre(request):
    return render(request, 'sobre.html')


def pesquisa(request):
    form = PesquisaServicoForm(request.GET)
    if form.is_valid():
        palavra = form.cleaned_data['nome']
        lista_servicos = Servico.objects.filter(nome__contains=palavra)
        paginator = Paginator(lista_servicos, 5)
        pagina = request.GET.get('pagina')
        servicos = paginator.get_page(pagina)
        if lista_servicos.count() == 0:
            messages.add_message(request, messages.ERROR, 'Nada foi encontrado.')
        return render(request, 'servico_listar.html', {'form': form, 'servicos': servicos})
    return redirect('estetica:pesquisa')


def servico_listar(request):
    form = PesquisaServicoForm(request.GET)
    servicos = Servico.objects.all().order_by('nome')
    current_user = request.user
    return render(request, 'servico_listar.html', {'servicos': servicos, 'form': form, 'user': current_user})


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
    return redirect('estetica:pesquisa')

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
            servico = servico_form.save(commit=False)
            if servico_id:
                servico.save()
                messages.add_message(request, messages.INFO, 'Serviço alterado com sucesso!')
            else:
                servico.user = request.user
                servico.save()
                messages.add_message(request, messages.INFO, 'Serviç!o cadastrado com sucesso')
            return redirect('estetica:pesquisa')
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        servico_form = ServicoForm()
    return render(request, 'servico_editar.html', {'form': servico_form})


def pacotes(request):
    servicos = Servico.objects.all().order_by('tipo__nome')
    return render(request, 'pacotes.html', {'servicos': servicos})
