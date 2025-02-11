from django.db import models
from django.utils import timezone

from titulo.models import Titulo


# Create your models here.
class Instrutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    rg = models.CharField(max_length=15, help_text="Informe o RG do Instrutor")
    nome = models.CharField(max_length=70, help_text="Informe o nome do Instrutor")    
    data_Nascimento = models.DateField(null=True, blank=True, help_text="Informe a data de nascimento do Instutor")    
    telefone = models.CharField(max_length=9, help_text="Informe o número do telefone do Instrutor")
    ddd = models.CharField(max_length=3, help_text="Informe o ddd do telefone do Instrutor")
    codigo_titulo = models.ForeignKey(Titulo, null=True, blank=True, on_delete=models.SET_NULL, db_column="titulo_codigo")

    def __str__(self):
        return f'{self.id} - {self.nome}'
