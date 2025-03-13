from django.urls import path
from . import views

app_name = 'aluno'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('carregarAluno/<int:matricula>', views.carregar_aluno, name='carregar_aluno'),
    path('excluir/<int:matricula>', views.excluir, name='excluir_aluno'),
    path('atualizarAluno', views.atualizar, name='atualizar_aluno'),
]

