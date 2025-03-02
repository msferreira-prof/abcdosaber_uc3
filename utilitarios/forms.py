from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=70, required=True, help_text="Informe o seu Nome")
    ultimoNome = forms.CharField(max_length=70, required=True, help_text="Informe o seu último Nome")
    email = forms.EmailField(required=True, help_text="Informe o seu E-mail")
    telefone = forms.CharField(max_length=10, required=True, help_text="Informe o seu Telefone")
    genero = forms.ChoiceField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')], required=False, help_text="Informe o seu Gênero")
    assunto = forms.ChoiceField(choices=[('E', 'Elogio'), ('C', 'Crítica'), ('S', 'Solicitação'), ('O', 'Outros')], required=False, help_text="Informe o Assunto")
    mensagem = forms.CharField(widget=forms.Textarea, required=True, help_text="Preencha com a mensagem desejada")
        
        