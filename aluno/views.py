from django.shortcuts import render, redirect
from django.http import HttpResponse

from aluno.models import Aluno
from aluno.forms import AlunoForm, AlunoAtualizarForm
from turma.models import Turma


# Create your views here.
def listar(request):
    
    # recuperar todos os alunos sem identificar se o aluno é monitor de alguma turma
    lista_aluno = Aluno.objects.all()
    
    contexto = {
        'alunos': lista_aluno,
    }
    
    return render(request, 'aluno/listarAluno.html', context=contexto)


def carregar_cadastro(request):
    return render(request, 'aluno/cadastrarAluno.html')


def cadastrar(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        dados_aluno = form.cleaned_data
        
        aluno = Aluno(
            nome = dados_aluno["nome"],
            data_Inicial = dados_aluno["data_Inicial"],
            data_Final = dados_aluno["data_Final"],
        )
        
        aluno.save()
    
    return render(request, 'aluno/cadastrarAluno.html')

    
def carregar_aluno(request, matricula):
    # recuperar o aluno a ser atualizado
    aluno = Aluno.objects.get(pk=matricula)
    contexto = {
        'aluno': aluno,
    }

    return render(request, 'aluno/atualizarAluno.html', context=contexto)

def excluir(request, matricula):
    aluno = Aluno.objects.get(pk=matricula)

    """
        Se o aluno for monitor de alguma turma, o campo matricula_monitor deverá ser atualiza com o valor Null
        antes de excluir o aluno.
    """
    turmas_monitoria = Turma.objects.filter(matricula_monitor=aluno.matricula)
    for turma in turmas_monitoria:
        turma.matricula_monitor = None
        turma.save()        
    
    aluno.delete()
    return redirect('aluno:listar')


def atualizar(request):
    if request.method == 'POST':
        form = AlunoAtualizarForm(request.POST)
        if form.is_valid():
            
            dados_aluno = form.cleaned_data
            
            matricula = request.POST.get('matricula')

            aluno = Aluno.objects.get(pk=matricula)

            aluno.nome = dados_aluno["nome"]
            aluno.data_inicial = dados_aluno["data_inicial"]
            aluno.data_final = dados_aluno["data_final"]
                    
            aluno.save()    
        else:
            print(form.errors)  # Print form errors to the console


    alunos = Aluno.objects.all()
    
    return render(request, 'aluno/listarAluno.html', { 'alunos': alunos })