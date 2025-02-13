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
    data_inicial = models.DateField(default=timezone.now(), help_text="Informe a data inicial da Turma")    
    data_final = models.DateField(default=timezone.now(), help_text="Informe a data final da Turma")
    codigo_atividade = models.ForeignKey(TipoDeAtividade, on_delete=models.CASCADE)
    matricula_monitor = models.ForeignKey(Aluno, null=True, blank=True, on_delete=models.SET_NULL)
    id_instrutor = models.ForeignKey(Instrutor, null=True, on_delete=models.CASCADE)
    
        
    class Meta:
        ordering = ['numero']
        
    def __str__(self):
        return f'{self.numero} - {self.id_instrutor.nome} - {self.matricula_monitor.nome}'