from django.shortcuts import render, redirect
from django.http import HttpResponse

from titulo.models import Titulo
from titulo.forms import TituloForm, TituloAtualizarForm
from instrutor.models import Instrutor


# Create your views here.
def listar(request):
    lista_titulo = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulo
    }
    
    return render(request, 'titulo/listarTitulo.html', context=contexto)

   
def carregar_cadastro(request):
    return render(request, 'titulo/cadastrarTitulo.html')


def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao = dados_titulo['descricao']
        )
        titulo.save()
    
    return render(request, 'titulo/cadastrarTitulo.html')
    

def carregar_titulo(request, codigo):
    # recuperar o titulo a ser atualizado
    titulo = Titulo.objects.get(pk=codigo)
    contexto = {
        'titulo': titulo,
    }

    return render(request, 'titulo/atualizarTitulo.html', context=contexto)


def excluir(request, codigo):
    titulo = Titulo.objects.get(pk=codigo)

    """
        Se o titulo não estiver relacionado a algum instrutor, 
        excluir o id do tipo informado.
    """
    
    instrutores = Instrutor.objects.filter(codigo_titulo=codigo)
    if not instrutores:
        titulo.delete()
    
    return redirect('titulo:listar')


def atualizar(request):
    if request.method == 'POST':
        form = TituloAtualizarForm(request.POST)
        if form.is_valid():
            
            dados_titulo = form.cleaned_data
    
            codigo = dados_titulo['codigo']
            
            titulo = Titulo.objects.get(pk=codigo)
            
            titulo.descricao = dados_titulo['descricao']

            titulo.save()

        # imprimir no console mensagens de erro da validação do formulário    
        # else:
        #     print(form.errors)  # Print form errors to the console

    return redirect('titulo:listar')

    