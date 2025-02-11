from django.shortcuts import render
from django.http import HttpResponse

from instrutor.models import Instrutor

# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    return HttpResponse(lista_instrutor)