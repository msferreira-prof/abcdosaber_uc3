from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def listar(request):
    return HttpResponse("Lista de Títulos")