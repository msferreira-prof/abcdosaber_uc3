from django import forms

class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descrição do Título")

class TituloAtualizarForm(forms.Form):
    codigo = forms.IntegerField(required=True, help_text="Informe o ID do Título")
    descricao = forms.CharField(max_length=70, required=True, help_text="Informe a descrição do Título")
    