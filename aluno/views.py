from django.shortcuts import render
from django.http import HttpResponse

from aluno.models import Aluno

# Create your views here.
def listar(request):
    lista_aluno = Aluno.objects.all()
    return HttpResponse(lista_aluno)