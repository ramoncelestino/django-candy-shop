from django import forms
from enderecos.models import Endereco

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'bairro']