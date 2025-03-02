from django.urls import path
from . import views

app_name = 'utilitarios'

urlpatterns = [
    path('carga/', views.popular_bd, name='popular'),
    path('contato/', views.carregar_contato, name='contato'),
    path('enviar/', views.enviar_mensagem_contato, name='enviar'),
]
