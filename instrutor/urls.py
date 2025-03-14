from django.urls import path
from . import views

app_name = 'instrutor'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('carregarInstrutor/<int:id>', views.carregar_instrutor, name='carregar_instrutor'),
    path('excluir/<int:id>', views.excluir, name='excluir_instrutor'),
    path('atualizarInstrutor', views.atualizar, name='atualizar_instrutor'),
]