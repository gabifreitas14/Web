from django import forms
from django.core.validators import RegexValidator

from meuSite.models import Servico, TipoServico


class PesquisaServicoForm(forms.Form):
    class Meta:
        fields = ('nome')

    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '120', 'placeholder': "Pesquise pelo nome do serviço"}),
        required=False)

    # <input type='text'
    #        name='nome'
    #        id='id_nome'
    #        class='form-control form-control-sm'
    #        maxlength='120'>


class RemoveServicoForm(forms.Form):
    class Meta:
        fields = 'servico_id'

    servico_id = forms.CharField(widget=forms.HiddenInput(), required=True)


class QuantidadeForm(forms.Form):
    class Meta:
        fields = ('quantidade', 'servico_id')

    # <input type="hidden" name="produto_id" id="id_produto_id" value="xxx">
    servico_id = forms.CharField(widget=forms.HiddenInput())

    quantidade = forms.IntegerField(
        min_value=1,
        max_value=1000,
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm quantidade',
                                      'maxlength': '20',
                                      'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'}),
        required=True)


class CarrinhoForm(forms.Form):
    class Meta:
        # model = Carrinho
        fields = ('servico_id', 'quantidade')

    servico_id = forms.CharField(widget=forms.HiddenInput())

    quantidade = forms.IntegerField(
        min_value=1,
        max_value=1000,
        error_messages={'required': 'Campo obrigatório.', },
        widget=forms.TextInput(attrs={'class': 'quantidade form-control form-control-sm text-center',
                                      'maxlength': '20',
                                      'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'}),
        required=True)


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ('servico_id', 'tipo', 'nome', 'preco', 'tag', 'imagem', 'descricao')

    servico_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    tipo = forms.ModelChoiceField(
        error_messages={'required': 'Campo obrigatório.', },
        queryset=TipoServico.objects.all().order_by('nome'),
        empty_label='--- Selecione um tipo ---',
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
        required=True)

    nome = forms.CharField(
        error_messages={'required': 'Campo obrigatório.',
                        'unique': 'Serviço duplicado.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
        required=True)

    # <input type="text"
    #        name="nome"
    #        id="id_nome"
    #        class="form-control form-control-sm"
    #        maxlength="120"
    #        required>

    tag = forms.CharField(
        error_messages={'required': 'Campo obrigatório.',
                        'unique': 'Tag duplicada.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '15'}),
        required=True)

    # <input type="text"
    #        name="preco"
    #        id="id_preco"
    #        class="form-control form-control-sm"
    #        maxlength="10"
    #        onkeypress="return (event.charCode >= 48 &amp;&amp; event.charCode <= 57) || event.charCode == 44"
    #        required="">

    imagem = forms.CharField(
        error_messages={'required': 'Campo obrigatório.',
                        'unique': 'Imagem duplicada.'},
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'maxlength': '120'}),
        required=True)

    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
        required=False)

    user_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    preco = forms.CharField(
        localize=True,
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(regex='^[0-9]{1,7}(,[0-9]{2})?$', message="Informe o valor no formato 9999999,99.")],
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'maxlength': '10',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || '
                                                    'event.charCode == 44'}),
        required=True)
