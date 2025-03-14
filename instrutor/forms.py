from django import forms

class InstrutorForm(forms.Form):
    rg = forms.CharField(max_length=15, required=False, help_text="Informe o RG do Instrutor")
    nome = forms.CharField(max_length=70, required=False, help_text="Informe o nome do Instrutor")    
    data_Nascimento = forms.DateField(required=True, help_text="Informe a data de nascimento do Instutor")    
    telefone = forms.CharField(max_length=9, required=False, help_text="Informe o número do telefone do Instrutor")
    ddd = forms.CharField(max_length=3, required=False, help_text="Informe o ddd do telefone do Instrutor")
    codigo_titulo = forms.IntegerField(required=True, help_text="Informe o título do Instrutor")


class InstrutorAtualizarForm(forms.Form):
    id = forms.IntegerField(required=True, help_text="Informe o id do Instrutor")
    rg = forms.CharField(max_length=15, required=False, help_text="Informe o RG do Instrutor")
    nome = forms.CharField(max_length=70, required=False, help_text="Informe o nome do Instrutor")    
    data_Nascimento = forms.DateField(required=True, help_text="Informe a data de nascimento do Instutor")    
    telefone = forms.CharField(max_length=9, required=False, help_text="Informe o número do telefone do Instrutor")
    ddd = forms.CharField(max_length=3, required=False, help_text="Informe o ddd do telefone do Instrutor")
    codigo_titulo = forms.IntegerField(required=True, help_text="Informe o título do Instrutor")
