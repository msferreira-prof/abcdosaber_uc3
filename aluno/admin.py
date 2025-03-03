from django.contrib import admin
from aluno.models import Aluno


# Register your models here.
# configura a tabela apresentada no app Admin
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'data_inicial', 'data_final')

admin.site.register(Aluno, AlunoAdmin)