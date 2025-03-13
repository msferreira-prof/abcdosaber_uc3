from django.contrib import admin

from turma.models import Turma, TurmaAluno, Ausencia

# Register your models here.
# configura a tabela apresentada no app Admin
class TurmaAdmin(admin.ModelAdmin): 
    list_display = ['numero', 'horario_aula', 'duracao_aula', 'data_inicial', 'data_final', 'codigo_atividade', 'matricula_monitor', 'id_instrutor']
class TurmaAlunoAdmin(admin.ModelAdmin): 
    list_display = ['numero_turma', 'matricula_aluno', 'data_inicio_matricula', 'data_fim_matricula']
# class AusenciaAdmin(admin.ModelAdmin): 
    # list_display = [field.name for field in Ausencia._meta.get_fields()]
    
admin.site.register(Turma, TurmaAdmin)
admin.site.register(TurmaAluno, TurmaAlunoAdmin)
admin.site.register(Ausencia) #, AusenciaAdmin)