from django.urls import path
from . import views

app_name = 'tipodeatividade'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('<int:ta_codigo>/', views.detalhe_tipodeatividade, name='detalhe'),
    path('cadastro/', views.carregar_cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('carregarTipoDeAtividade/<int:codigo>', views.carregar_tipodeatividade, name='carregar_tipodeatividade'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_tipodeatividade'),
    path('atualizarTipoDeAtividade', views.atualizar, name='atualizar_tipodeatividade'),
]
