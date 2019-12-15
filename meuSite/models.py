from django.conf import settings
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
    tag = models.SlugField('Tag', max_length=100, default=' ')
    imagem = models.CharField('Imagem', max_length=200)
    descricao = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='servicos',
                             on_delete=models.DO_NOTHING,
                             null=True)
    preco = models.DecimalField('Preco', max_digits=10, decimal_places=2, default=0)

    # preco = models.DecimalField(max_digits=10, decimal_places=2)
    # estoque = models.PositiveIntegerField()
    # disponivel = models.BooleanField(default=True)

    class Meta:
        db_table = 'servico'
        ordering = ('nome',)

    def get_absolute_path(self):
        return reverse('estetica:servico', args=[self.id, self.tag])

    def __str__(self):
        return self.nome


class DestaqueServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True, blank=True)
    fraseDestaque = models.CharField('Frase', max_length=200, blank=True)
    descricao = models.TextField(blank=True)
    likes = models.IntegerField('likes', default=0)
    dislikes = models.IntegerField('dislikes', default=0)
    ordem = models.IntegerField('ordem', default=0)

    class Meta:
        db_table = 'destaqueServico'

    # def get_absolute_path(self):
    #     return reverse('estetica:facial')

    def __str__(self):
        return self.servico.nome


# class Carrinho(models.Model):
#     servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              related_name="usuario",
#                              on_delete=models.DO_NOTHING,
#                              null=True)
#     quantidade = models.IntegerField(default=0)
#     preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#
#     class Meta:
#         db_table = 'carrinho'


class FotoCarousel(models.Model):
    nome = models.CharField('nome', max_length=200, blank=True)
    endereco = models.CharField('Imagem', max_length=200)

    class Meta:
        db_table = 'fotoCarousel'

    # def get_absolute_path(self):
    #     return reverse('estetica:facial')

    def __str__(self):
        return self.nome
