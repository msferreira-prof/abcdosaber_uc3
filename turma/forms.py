from django import forms
from django.utils import timezone

class TurmaForm(forms.Form):
    horario_aula = forms.TimeField(required=True, help_text="Informe a hora em que a hora da aula da Turma")
    duracao_aula = forms.IntegerField(required=True, initial=30, help_text="Informe a duração da aula da Turma")
    data_inicial = forms.DateField(required=True, initial=timezone.now, help_text="Informe a data inicial da Turma")    
    data_final = forms.DateField(required=False, help_text="Informe a data final da Turma")
    codigo_atividade = forms.IntegerField(required=True, help_text="Informe o código da atividade da Turma")    
    matricula_monitor = forms.IntegerField(required=False, help_text="Informe a matrícula do monitor da Turma")
    id_instrutor = forms.IntegerField(required=False, help_text="Informe o id do instrutor da Turma")

    
class TurmaAlunoForm(forms.Form):
    numero_turma =  forms.IntegerField(required=True, help_text="Número da turma do aluno.")       
    matricula_aluno = forms.IntegerField(required=True, help_text="Matrícula do aluno da turma")
    data_inicio_matricula = forms.DateField(required=True, initial=timezone.now, help_text="Data da matrícula do aluno na turma")
    data_fim_matricula = forms.DateField(required=False, help_text="Data de fim de matrícula do aluno na turma")    


class TurmaAusenciaForm(forms.Form):
    numero_turma = forms.IntegerField(required=True,  help_text="Número da turma do aluno.")       

      
class AusenciaForm(forms.Form):
    numero_turma =  forms.IntegerField(required=True,  help_text="Número da turma do aluno.")       
    matricula_aluno = forms.IntegerField(required=True, help_text="Matrícula do aluno da turma")
    data_ausencia = forms.DateField(required=True, initial=timezone.now, help_text="Data da falta do aluno na turma")
