from django.contrib import admin
from tipodeatividade.models import TipoDeAtividade

# Register your models here.
# configura a tabela apresentada no app Admin
class TipoDeAtividadeAdmin(admin.ModelAdmin): 
    list_display = ('codigo', 'descricao')

admin.site.register(TipoDeAtividade, TipoDeAtividadeAdmin)

