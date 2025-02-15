from django.contrib import admin

from turma.models import Turma, TurmaAluno, Ausencia

# Register your models here.
admin.site.register(Turma)
admin.site.register(TurmaAluno)
admin.site.register(Ausencia)
