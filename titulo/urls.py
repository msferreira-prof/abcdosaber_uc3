from django.urls import path
from . import views

app_name = 'titulo'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('carregarTitulo/<int:codigo>', views.carregar_titulo, name='carregar_titulo'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_titulo'),
    path('atualizarTitulo', views.atualizar, name='atualizar_titulo'),
]
