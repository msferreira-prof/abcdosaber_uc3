from django.urls import path
from . import views

app_name = 'tipodeatividade'

urlpatterns = [
    path('lista/', views.listar, name='listar'),
    path('<int:ta_codigo>/', views.detalhe_tipodeatividade, name='tipodeatividade')
]
