from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('carregar_turmas/', views.carregar_ausencia_turma, name='carregar_turmas'),
    path('carregar_alunos_turma/', views.carregar_ausencia_turma_alunos, name='carregar_alunos_turma'),
    path('registrar_ausencia/', views.registrar_ausencia, name='registrar_ausencia'),
]