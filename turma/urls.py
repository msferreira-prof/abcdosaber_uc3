from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.listar, name='listar'),
]
