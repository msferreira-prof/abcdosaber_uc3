from django.shortcuts import render
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade

# Create your views here.
def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    contexto = {
        'tiposdeatividade': lista_tipodeatividade
    }
    
    return render(request, 'tipodeatividade/listarTipoDeAtividade.html', context=contexto)

   
def detalhe_tipodeatividade(request, ta_codigo):
    tipodeatividade = TipoDeAtividade.objects.get(pk=ta_codigo)
    return HttpResponse(tipodeatividade)