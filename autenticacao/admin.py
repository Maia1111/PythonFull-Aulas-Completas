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

    
class Pessoa(admin.ModelAdmin):
    list_display = ('campo1', 'campo2', 'botao_salvar')

    def botao_salvar(self, obj):
        return '<button type="submit">Salvar</button>'

    botao_salvar.short_description = "Salvar"






