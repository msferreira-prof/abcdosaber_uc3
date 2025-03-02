from django.shortcuts import render
from django.http import HttpResponse

from aluno.models import Aluno
from aluno.forms import AlunoForm


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
    