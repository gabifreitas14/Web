from decimal import Decimal

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from meuSite.forms import ServicoForm, RemoveServicoForm, PesquisaServicoForm, CarrinhoForm, QuantidadeForm
from .models import FotoCarousel, DestaqueServico, Servico
from django.core.paginator import Paginator
from django.db.models import Sum, F, FloatField
from meuSite.carrinho import Carrinho


def index(request):
    fotos_carousel = FotoCarousel.objects.all()
    destaques = DestaqueServico.objects.all().order_by('ordem')

    return render(request, 'index.html', {'fotos_carousel': fotos_carousel, 'destaques': destaques})


def facial(request):
    procedimentos_faciais = Servico.objects.filter(tipo__nome__contains='facial')
    return render(request, 'facial.html', {'servicos': procedimentos_faciais})


def corporal(request):
    corporais = Servico.objects.filter(tipo__nome__contains='corporal')
    return render(request, 'corporal.html', {'servicos': corporais})


def servico(request, servico_id, tag_servico):
    serv = get_object_or_404(Servico, id=servico_id)
    user = request.user
    carrinho_form = CarrinhoForm(initial={'quantidade': 1, 'user': user.id, 'servico_id': servico_id})
    return render(request, 'servico.html', {'servico': serv, 'form_servico': carrinho_form})


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
                messages.add_message(request, messages.INFO, 'Serviço cadastrado com sucesso')
            return redirect('estetica:pesquisa')
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        servico_form = ServicoForm()
    return render(request, 'servico_editar.html', {'form': servico_form})


def pacotes(request):
    servicos = Servico.objects.all().order_by('tipo__nome')
    paginator = Paginator(servicos, 6)
    pagina = request.GET.get('pagina')
    servicos_paginados = paginator.get_page(pagina)
    lista_de_forms = []
    user = request.user
    for servico in servicos_paginados:
        lista_de_forms.append(CarrinhoForm(initial={'quantidade': 0, 'servico_id': servico.id, 'user': user.id}))
    return render(request, 'pacotes.html', {'lista_forms': zip(servicos_paginados, lista_de_forms)})


def exibe_carrinho(request):
    carrinho = Carrinho(request)
    lista_itens = carrinho.get_servico()
    servicos_no_carrinho = []
    lista_de_forms = []
    total = 0
    for item in lista_itens:
        servicos_no_carrinho.append(item['servico'])
        lista_de_forms.append(CarrinhoForm(initial={'quantidade': item['quantidade']}))
        total += int(item['quantidade']) * Decimal(item['preco'])

    return render(request, 'carrinho.html',
                  {'listas': zip(servicos_no_carrinho, lista_de_forms) if len(servicos_no_carrinho) > 0 else None,
                   'total': total})


def remove_servico_carrinho(request):
    form = RemoveServicoForm(request.POST)
    if form.is_valid():
        carrinho = Carrinho(request)
        carrinho.remover(form.cleaned_data['servico_id'])

        return exibe_carrinho(request)

    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')


def adicionar_ao_carrinho(request):
    form = CarrinhoForm(request.POST)
    # servico_id = request.POST.get('servico_id')
    if form.is_valid():
        quantidade = form.cleaned_data['quantidade']
        servico_id = form.cleaned_data["servico_id"]
        carrinho_novo = Carrinho(request)
        carrinho_novo.adicionar(servico_id, quantidade)
        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao adicionar um  produto ao carrinho')


def atualiza_qtd_carrinho(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        servico_id = form.cleaned_data['servico_id']
        quantidade = form.cleaned_data['quantidade']

        carrinho = Carrinho(request)
        carrinho.alterar(servico_id, quantidade)

        return exibe_carrinho(request)
    else:
        print(form.errors)
        raise ValueError('Ocorreu um erro inesperado ao alterar um serviço ao carrinho.')
