from django.shortcuts import render
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividadeForm
   

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

 
def carregar_cadastro(request):
    return render(request, 'tipodeatividade/cadastrarTipoDeAtividade.html')


def cadastrar(request):
    form = TipoDeAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        tipodeatividade = TipoDeAtividade(
            descricao = dados_tipodeatividade['descricao']
        )
        
        tipodeatividade.save()
    
    return render(request, 'tipodeatividade/cadastrarTipoDeAtividade.html')
    
    