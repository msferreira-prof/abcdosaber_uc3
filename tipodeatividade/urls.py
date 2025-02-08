from django.urls import path
from . import views

urlpatterns = [
    path('indice', views.index, name='index'),
    path('lista/', views.listar, name='listar'),
    path('bomdia/', views.show_mensagem, name='bomdia'),
    path('<int:ta_codigo>/', views.detalhe_tipodeatividade, name='tipodeatividade')
]
