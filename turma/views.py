from django.shortcuts import render
from django.http import HttpResponse

from turma.models import Turma, Ausencia
from instrutor.models import Instrutor
from tipodeatividade.models import TipoDeAtividade
from aluno.models import Aluno
from turma.forms import TurmaForm, TurmaAlunoForm, AusenciaForm, TurmaAusenciaForm

# Create your views here.
def listar(request):
    lista_turmas = Turma.objects.all()
    contexto = {
        'turmas': lista_turmas
    }
    
    return render(request, 'turma/listarTurma.html', context=contexto)

   
def carregar_cadastro(request):
    lista_tiposdeatividade = TipoDeAtividade.objects.all()
    lista_instrutores = Instrutor.objects.all()
    lista_alunos = Aluno.objects.all()
    
    contexto = {
        'tiposdeatividade': lista_tiposdeatividade,
        'instrutores': lista_instrutores,
        'alunos': lista_alunos,        
    }
    return render(request, 'turma/cadastrarTurma.html', context=contexto)


def cadastrar(request):
    form = TurmaForm(request.POST)
    if form.is_valid():
        dados_turma = form.cleaned_data
        
        # recuperando o objeto Titulo com a chave primaria informada no formulario do instrutor
        # se vier zero do formulario, é porque o titulo nao foi selecionado e o objeto titulo sera None
        tipo_de_atividade = None
        if dados_turma["codigo_atividade"] != "0":
            tipo_de_atividade = TipoDeAtividade.objects.get(pk=dados_turma["codigo_atividade"])
                
        instrutor = None
        if dados_turma["id_instrutor"] != "0":
            instrutor = Instrutor.objects.get(pk=dados_turma["id_instrutor"])
                
        aluno = None
        if dados_turma["matricula_monitor"] != "0":
            aluno = Aluno.objects.get(pk=dados_turma["matricula_monitor"])
                
        turma = Turma(
            horario_aula = dados_turma["horario_aula"],
            duracao_aula = dados_turma["duracao_aula"],
            data_inicial = dados_turma["data_inicial"],
            data_final = dados_turma["data_final"],
            codigo_atividade = tipo_de_atividade,
            matricula_monitor = aluno,
            id_instrutor = instrutor,
        )
        
        turma.save()
    
    lista_tiposdeatividade = TipoDeAtividade.objects.all()
    lista_instrutores = Instrutor.objects.all()
    lista_alunos = Aluno.objects.all()

    contexto = {
        'tiposdeatividade': lista_tiposdeatividade,
        'instrutores': lista_instrutores,
        'alunos': lista_alunos,        
    }
    
    return render(request, 'turma/cadastrarTurma.html', context=contexto)
    

# ausencia
def carregar_ausencia_turma(request):
    lista_turmas = Turma.objects.all()
        
    contexto = {
        'turmas': lista_turmas,        
    }
    return render(request, 'turma/registrarAusencia.html', context=contexto)

def carregar_ausencia_turma_alunos(request):
    
    form = TurmaAusenciaForm(request.POST)
    if form.is_valid():
        turma = form.cleaned_data
    
        turma = Turma.objects.get(pk=turma["numero_turma"])
        lista_alunos = turma.alunos.get(pk=turma.numero)
        
        contexto = {
            'alunos': lista_alunos,        
        }
        
    return render(request, 'turma/registrarAusencia.html', context=contexto)
    

def registrar_ausencia(request):
    
    form = AusenciaForm(request.POST)
    if form.is_valid():
        dados_ausencia = form.cleaned_data
        
        # recuperando o objeto Titulo com a chave primaria informada no formulario do instrutor
        # se vier zero do formulario, é porque o titulo nao foi selecionado e o objeto titulo sera None
        turma = Turma.objects.get(pk=dados_ausencia['numero_turma'])
        aluno = Aluno.objects.get(pk=dados_ausencia["matricula"])
                
        ausencia = Ausencia(
            numero_turma = turma,
            matricula_aluno = aluno,
            data_ausencia = dados_ausencia["data_ausencia"],
        )
        
        ausencia.save()
    
    carregar_ausencia_turma(request)
    