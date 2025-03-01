from django.shortcuts import render
from django.http import HttpResponse

from instrutor.models import Instrutor
from titulo.models import Titulo
from instrutor.forms import InstrutorForm

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
    