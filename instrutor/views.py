from django.shortcuts import render, redirect
from django.http import HttpResponse

from instrutor.models import Instrutor
from titulo.models import Titulo
from instrutor.forms import InstrutorForm, InstrutorAtualizarForm
from turma.models import Turma


# Create your views here.
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutor
    }
    
    return render(request, 'instrutor/listarInstrutor.html', context=contexto)

   
def carregar_cadastro(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render(request, 'instrutor/cadastrarInstrutor.html', context=contexto)


def cadastrar(request):
    form = InstrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        
        # recuperando o objeto Titulo com a chave primaria informada no formulario do instrutor
        # se vier zero do formulario, é porque o titulo nao foi selecionado e o objeto titulo sera None
        titulo = None
        if dados_instrutor["codigo_titulo"] != "0":
            titulo = Titulo.objects.get(pk=dados_instrutor["codigo_titulo"])
                
        instrutor = Instrutor(
            rg = dados_instrutor["rg"],
            nome = dados_instrutor["nome"],
            data_Nascimento = dados_instrutor["data_Nascimento"],
            telefone =dados_instrutor["telefone"],
            ddd = dados_instrutor["ddd"],
            codigo_titulo = titulo,
        )
        
        instrutor.save()
    
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render(request, 'instrutor/cadastrarInstrutor.html', context=contexto)


def carregar_instrutor(request, id):
    # carregar a lista de titulos para preencher o campo select do formulario
    lista_titulos = Titulo.objects.all()

    # recuperar o instrutor a ser atualizado
    instrutor = Instrutor.objects.get(pk=id)
    contexto = {
        'instrutor': instrutor,
        'titulos': lista_titulos,
    }

    return render(request, 'instrutor/atualizarInstrutor.html', context=contexto)


def excluir(request, id):
    instrutor = Instrutor.objects.get(pk=id)

    """
        Se o instrutor for instrutor de alguma turma, o campo id_instrutor deverá ser atualiza com o valor Null
        antes de excluir o instrutor.
    """
    turmas_instrutoria = Turma.objects.filter(id_instrutor=instrutor.id)
    for turma in turmas_instrutoria:
        turma.id_instrutor = None
        turma.save()        
    
    instrutor.delete()
    
    return redirect('instrutor:listar')


def atualizar(request):
    if request.method == 'POST':
        form = InstrutorAtualizarForm(request.POST)
        if form.is_valid():
            
            dados_instrutor = form.cleaned_data
            
            id = request.POST.get('id')

            instrutor = Instrutor.objects.get(pk=id)

            instrutor.rg = dados_instrutor["rg"]
            instrutor.nome = dados_instrutor["nome"]
            instrutor.data_Nascimento = dados_instrutor["data_Nascimento"]
            instrutor.telefone = dados_instrutor["telefone"]
            instrutor.ddd = dados_instrutor["ddd"]

            # recuperando o objeto Titulo com a chave primaria informada no formulario do instrutor
            # se vier zero do formulario, é porque o titulo nao foi selecionado e o objeto titulo sera None
            titulo = None
            if dados_instrutor["codigo_titulo"] != "0":
                titulo = Titulo.objects.get(pk=dados_instrutor["codigo_titulo"])
            instrutor.codigo_titulo = titulo
            
            instrutor.save()    

        # imprimir no console mensagens de erro da validação do formulário        
        else:
            print(form.errors)  # Print form errors to the console

    return redirect('instrutor:listar')
    