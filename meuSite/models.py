from django.db import models
from django.urls import reverse


class TipoServico(models.Model):
    nome = models.CharField('Tipo', max_length=200, db_index=True, unique=True)
    nomePrincipal = models.CharField('Nome Principal', max_length=200, db_index=True, unique=True)

    class Meta:
        db_table = 'tipoServico'

    # def get_absolute_path(self):
    #     return reverse('estetica:facial')

    def __str__(self):
        return self.nome


class Servico(models.Model):
    tipo = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    nome = models.CharField('Servico', max_length=200, db_index=True)
    imagem = models.CharField('Imagem', max_length=200)
    descricao = models.TextField(blank=True)

    # preco = models.DecimalField(max_digits=10, decimal_places=2)
    # estoque = models.PositiveIntegerField()
    # disponivel = models.BooleanField(default=True)

    class Meta:
        db_table = 'servico'

    # def get_absolute_path(self):
    #     return reverse('produto:exibe_produto', args=[self.id, self.slug])

    def __str__(self):
        return self.nome


class DestaqueServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    fraseDestaque = models.CharField('Frase', max_length=200, blank=True)
    descricao = models.TextField(blank=True)
    likes = models.IntegerField('likes', max_length=10000, default=0)
    dislikes = models.IntegerField('dislikes', max_length=10000, default=0)

    class Meta:
        db_table = 'destaqueServico'

    # def get_absolute_path(self):
    #     return reverse('estetica:facial')

    def __str__(self):
        return self.servico.nome


class FotoCarousel(models.Model):
    nome = models.CharField('nome', max_length=200, blank=True)
    endereco = models.CharField('Imagem', max_length=200)

    class Meta:
        db_table = 'fotoCarousel'

    # def get_absolute_path(self):
    #     return reverse('estetica:facial')

    def __str__(self):
        return self.nome
