from django.shortcuts import render
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
