from django.contrib import admin
from instrutor.models import Instrutor

# Register your models here.
# configura a tabela apresentada no app Admin
class InstrutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'rg', 'nome', 'data_Nascimento', 'ddd', 'telefone', 'codigo_titulo')


admin.site.register(Instrutor, InstrutorAdmin)