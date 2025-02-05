from django.db import models
from django.urls import reverse

# Create your models here.
class TipoDeAtividade(models.Model):
    codigo = models.IntegerField(primary_key=True, 
                                 help_text='Código do Tipo de Atividade')
    descricao = models.CharField(max_length=70, null=False,
                                 help_text='Informe a descrição do Tipo de Atividade')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'    
