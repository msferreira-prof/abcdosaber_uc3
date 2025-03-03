from django.contrib import admin
from titulo.models import Titulo


# Register your models here.
# configura a tabela apresentada no app Admin
class TituloAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao')

admin.site.register(Titulo, TituloAdmin)
