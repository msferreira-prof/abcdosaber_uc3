from django.shortcuts import render, redirect
from django.http import HttpResponse

from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividadeForm, TipoDeAtividadeAtualizarForm
from turma.models import Turma   

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

    
def carregar_tipodeatividade(request, codigo):
    # recuperar o tipo de atividade a ser atualizado
    tipodeatividade = TipoDeAtividade.objects.get(pk=codigo)
    contexto = {
        'tipodeatividade': tipodeatividade,
    }

    return render(request, 'tipodeatividade/atualizarTipoDeAtividade.html', context=contexto)


def excluir(request, codigo):
    tipodeatividade = TipoDeAtividade.objects.get(pk=codigo)

    """
        Se o tipo de atividade não estiver relacionado a alguma turma, 
        excluir o codigo do tipo informado.
    """
    
    turmas = Turma.objects.filter(codigo_atividade=codigo)
    if not turmas:
        tipodeatividade.delete()
    
    return redirect('tipodeatividade:listar')


def atualizar(request):
    if request.method == 'POST':
        form = TipoDeAtividadeAtualizarForm(request.POST)
        if form.is_valid():
            
            dados_tipodeatividade = form.cleaned_data
    
            codigo = dados_tipodeatividade['codigo']
            
            tipodeatividade = TipoDeAtividade.objects.get(pk=codigo)
            
            tipodeatividade.descricao = dados_tipodeatividade['descricao']

            tipodeatividade.save()
    
        # imprimir no console mensagens de erro da validação do formulário
        # else:
        #     print(form.errors)  # Print form errors to the console

    return redirect('tipodeatividade:listar')

