from django.db import models
from django.utils import timezone

from tipodeatividade.models import TipoDeAtividade
from instrutor.models import Instrutor
from aluno.models import Aluno


# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text="Informe a turma do Aluno")
    horario_aula = models.TimeField(help_text="Informe a hora em que a hora da aula da Turma")
    duracao_aula = models.SmallIntegerField(default=30, help_text="Informe a duração da aula da Turma")
    data_inicial = models.DateField(default=timezone.now, help_text="Informe a data inicial da Turma")    
    data_final = models.DateField(null=True, blank=True, help_text="Informe a data final da Turma")
    codigo_atividade = models.ForeignKey(TipoDeAtividade, on_delete=models.CASCADE)
    matricula_monitor = models.ForeignKey(Aluno, null=True, blank=True, on_delete=models.SET_NULL)
    id_instrutor = models.ForeignKey(Instrutor, null=True, on_delete=models.CASCADE)
    
        
    class Meta:
        ordering = ['numero']
        
    def __str__(self):
        return f'Turma: {self.numero} - Instrutor: {self.id_instrutor.nome} - Monitor: {self.matricula_monitor.nome}'
    
class TurmaAluno(models.Model):
    numero_turma =  models.ForeignKey(Turma, on_delete=models.CASCADE, 
                                      help_text="Número da turma do aluno.")       
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE,
                                        help_text="Matrícula do aluno da turma")
    data_inicio_matricula = models.DateField(null=False,
                                             default=timezone.now,
                                             help_text="Data da matrícula do aluno na turma")
    data_fim_matricula = models.DateField(null=True, blank=True,
                                          help_text="Data de fim de matrícula do aluno na turma")    
    
    def __str__(self):
        resposta = f'Turma: {self.id} - Aluno: {self.matricula_aluno}'
        return resposta
    
class Ausencia(models.Model):
    numero_turma =  models.ForeignKey(Turma, on_delete=models.CASCADE, 
                                      help_text="Número da turma do aluno.")       
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE,
                                        help_text="Matrícula do aluno da turma")
    data_ausencia = models.DateField(null=False,
                                     default=timezone.now,
                                     help_text="Data da falta do aluno na turma")

    def __str__(self):
        resposta = f'Turma: {self.numero_turma} - Aluno: {self.matricula_aluno} - Dt Ausência: {self.data_ausencia.strftime("%d/%m/%y")}'
        return resposta