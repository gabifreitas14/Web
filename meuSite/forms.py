from django import forms
from meuSite.models import Servico, TipoServico


class PesquisaServicoForm(forms.Form):
    class Meta:
        fields = ('nome')

    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '120', 'placeholder': "Pesquise pelo nome do serviço"}),
        required=False)

    # <input type='text'
    #        name='nome'
    #        id='id_nome'
    #        class='form-control form-control-sm'
    #        maxlength='120'>


class RemoveServicoForm(forms.Form):
    class Meta:
        fields = ('servico_id')

    servico_id = forms.CharField(widget=forms.HiddenInput(), required=True)


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ('servico_id', 'tipo', 'nome', 'tag', 'imagem', 'descricao')

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