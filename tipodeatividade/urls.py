from django.urls import path
from . import views

urlpatterns = [
    path('indice/', views.index, name='index'),
    path('lista/', views.listar, name='listar'),
]
