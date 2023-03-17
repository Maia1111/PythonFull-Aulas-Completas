from django.contrib import admin
from autenticacao.models import Pessoa, Cargos, Pedido



class PedidoInline(admin.TabularInline):
    list_display  = ('nome', 'quantidade', 'descricao')
    model = Pedido
    extra = 3

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display = ('get_foto', 'nome', 'email', 'senha', 'nome_completo',)
    search_fields = ('nome',)
    list_filter = ('cargo',)


admin.site.register(Pedido)
admin.site.register(Cargos)



