from datetime import date, timedelta
import random
from django.db import connection

from tipodeatividade.models import TipoDeAtividade
from titulo.models import Titulo
from aluno.models import Aluno
from instrutor.models import Instrutor
from turma.models import Turma, TurmaAluno, Ausencia


# geracao de valores aleatorios
def gerar_numero_aleatorio_faixa(ini, fim):
    return random.randint(ini, fim)

def gerar_numero_aleatorio_sequencia(sequencia):
    return random.choice(sequencia)

def gerar_horario_aleatorio():
    return random.choice(['08:00', '13:00', '18:00'])

def gerar_duracao_aleatoria():
    return random.choice([120, 240])

def gerar_data_aleatoria(tipo_data):
    dia = gerar_numero_aleatorio_faixa(1, 28)
    mes = gerar_numero_aleatorio_faixa(1, 12)
    ano = 0
    if tipo_data == 'inicial':
        ano = gerar_numero_aleatorio_faixa(1970, 2007)
    else:
        ano = gerar_numero_aleatorio_faixa(2021, 2024)
    
    return date(ano, mes, dia)


# apagar tabelas
def apagar_registros():
    if TurmaAluno.objects.exists():
        TurmaAluno.objects.all().delete()
    if Ausencia.objects.exists():
        Ausencia.objects.all().delete()
    if Turma.objects.exists():
        Turma.objects.all().delete()
    if Instrutor.objects.exists():
        Instrutor.objects.all().delete()
    if Aluno.objects.exists():
        Aluno.objects.all().delete()
    if Titulo.objects.exists():
        Titulo.objects.all().delete()
    if TipoDeAtividade.objects.exists():
        TipoDeAtividade.objects.all().delete()

             
# truncar tabelas para zerar o contador de auto-incremento
def truncate_table(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM {table_name}')
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}"')  # Reset auto-increment counter

# executar o truncate
def truncar_tabelas():
    truncate_table('turma_turmaaluno')
    truncate_table('turma_ausencia')
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tipodeatividade_tipodeatividade')


# popular tabelas
def popular_tipodeatividade():

    lista_tipodeatividade = []
    
    for i in range(1, 10):
        lista_tipodeatividade.append(TipoDeAtividade(descricao='Atividade ' + f'{i:02}'))
        
    TipoDeAtividade.objects.bulk_create(lista_tipodeatividade)


def popular_titulo():

    lista_titulo = []
    
    for i in range(1, 10):
        lista_titulo.append(Titulo(descricao='Titulo ' + f'{i:02}'))
        
    Titulo.objects.bulk_create(lista_titulo)


def popular_aluno():

    lista_aluno = []
    
    for i in range(1, 50):
        
        lista_aluno.append(
            Aluno(
                nome='Aluno ' + f'{i:02}',
                data_inicial=gerar_data_aleatoria('inicial')
            )
        )
        
    Aluno.objects.bulk_create(lista_aluno)


def popular_instrutor():

    lista_instrutor = []
    
    for i in range(1, 10):
        
        titulo = Titulo.objects.get(pk=gerar_numero_aleatorio_sequencia(Titulo.objects.values_list('codigo', flat=True)))
        
        lista_instrutor.append(
            Instrutor(
                nome = 'Instrutor ' + f'{i:02}',
                data_Nascimento = gerar_data_aleatoria('nascimento'),
                rg = f'{gerar_numero_aleatorio_faixa(1, 99999999999):011}',
                telefone = f'{gerar_numero_aleatorio_faixa(1, 999999999):09}',
                ddd = f'{gerar_numero_aleatorio_faixa(1, 60):03}',
                codigo_titulo = titulo,
            )
        )
        
    Instrutor.objects.bulk_create(lista_instrutor)
    
    
def popular_turma():

    lista_turma = []
    
    for i in range(1, 10):

        tipodeatividade = TipoDeAtividade.objects.get(pk=gerar_numero_aleatorio_sequencia(TipoDeAtividade.objects.values_list('codigo', flat=True)))
        aluno = Aluno.objects.get(pk=gerar_numero_aleatorio_sequencia(Aluno.objects.values_list('matricula', flat=True)))
        instrutor = Instrutor.objects.get(pk=gerar_numero_aleatorio_sequencia(Instrutor.objects.values_list('id', flat=True)))
        
        lista_turma.append(
            Turma(
                horario_aula = gerar_horario_aleatorio(),
                duracao_aula = gerar_duracao_aleatoria(),
                data_inicial = gerar_data_aleatoria('inicial'),
                codigo_atividade = tipodeatividade,
                matricula_monitor = aluno,
                id_instrutor = instrutor,
            )
        )
        
    Turma.objects.bulk_create(lista_turma)
    

def popular_turma_aluno():

    lista_turma_aluno = []
    
    for i in range(1, 10):
        
        turma = Turma.objects.get(pk=gerar_numero_aleatorio_sequencia(Turma.objects.values_list('numero', flat=True)))
        
        alunos = []
        
        for j in range(1, 5):
            aluno = Aluno.objects.get(pk=gerar_numero_aleatorio_sequencia(Aluno.objects.values_list('matricula', flat=True)))
            
            # eliminando duplicidade de aluno na mesma turma
            if aluno not in alunos:
                alunos.append(aluno)
            else:
                alunos.remove(aluno)
            
        for aluno in alunos:    
            lista_turma_aluno.append(
                TurmaAluno(
                    numero_turma = turma,
                    matricula_aluno = aluno,
                    data_inicio_matricula = turma.data_inicial,
                )
            )
                
    TurmaAluno.objects.bulk_create(lista_turma_aluno)


def popular_turma_ausencia():

    lista_ausencia = []
    
    for i in range(1, 10):
        turma_aluno = TurmaAluno.objects.get(pk=gerar_numero_aleatorio_sequencia(TurmaAluno.objects.values_list('id', flat=True)))
        
        # a = turma_aluno.get(pk=1)        
        # print('alunos')
        # print()
        # print(a)
        
        alunos = turma_aluno.matricula_aluno.objects.all()
        
        for aluno in alunos:
            
            ausencia = Ausencia (
                    numero_turma = turma_aluno,
                    matricula_aluno = aluno, 
                    data_ausencia = turma_aluno.numero_turma.data_inicial + timedelta(days=i),
                )
            
            lista_ausencia.append(ausencia)
  
    #print(lista_ausencia)          
    Ausencia.objects.bulk_create(lista_ausencia)