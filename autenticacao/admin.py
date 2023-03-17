from django.contrib import admin
from autenticacao.models import Pessoa, Cargos, Pedido
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse



admin.site.register(Pedido)
admin.site.register(Cargos)

class PedidoInline(admin.TabularInline):
    list_display  = ('nome', 'quantidade', 'descricao')
    model = Pedido
    extra = 3

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin, DjangoObjectActions):
    inlines = [PedidoInline]
    list_display = ('get_foto', 'nome', 'email', 'senha', 'nome_completo',)
    search_fields = ('nome',)
    list_filter = ('cargo',)

    def mostra_pessoa(self, request, pessoa):
        return HttpResponse('Teste')
    
    mostra_pessoa.label = "mostra pessoa"
    change_actions = ("mostra_pessoa",)

    





