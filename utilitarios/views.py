from django.shortcuts import redirect, render
from django.core.mail import send_mail

from abcdosaber.settings import EMAIL_HOST_USER
from utilitarios import utils
from utilitarios.forms import ContatoForm

# Create your views here.
def popular_bd(request):
    utils.truncar_tabelas()
    #utils.apagar_registros()
    utils.popular_tipodeatividade()
    utils.popular_titulo()
    utils.popular_aluno()
    utils.popular_instrutor()
    utils.popular_turma()
    utils.popular_turma_aluno()
    utils.popular_turma_ausencia()
        
    return redirect('/')


def carregar_contato(request):
    return render(request, 'utilitarios/contato.html')


def enviar_mensagem_contato(request):
    
    form = ContatoForm(request.POST)
    if form.is_valid():
        dados_mensagem = form.cleaned_data
        
        assunto = dados_mensagem['assunto']
        mensagem = dados_mensagem['mensagem']
        email_destino = [ dados_mensagem['email'] ]

        # procure por EMAIL_HOST_USER e EMAIL_HOST_PASSWORD no settings.py
        email_origem = EMAIL_HOST_USER
                
        # enviando um email
        # será necessário configurar o EMAIL_HOST_USER e EMAIL_HOST_PASSWORD, bem como, as constantes definidas no settings.py, 
        # caso contrario, o email não será enviado e será exibido um erro
        # procure o comentário "Configuração de envio de e-mail no settings.py"
        send_mail(
            assunto,  # assunto
            mensagem,  # mensagem
            email_origem,  # from email
            email_destino,  # to email
            fail_silently = False,
        )
    
    return redirect('/')