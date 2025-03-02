from django import forms

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=70, required=True, help_text="Informe o nome do Aluno")
    data_inicial = forms.DateField(required=True, help_text="Informe a data inicial de matrícula do Aluno")    
    data_final = forms.DateField(required=False, help_text="Informe a data final de matrícula do Aluno")
    
    