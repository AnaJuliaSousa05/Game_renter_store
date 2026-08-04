from django.contrib import admin
from .models import Jogo, Locacao

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'preco_diaria', 'alugado')
    list_editable = ('alugado',)

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'jogo', 'data_locacao', 'data_devolucao', 'valor_total', 'devolvido')
    list_filter = ('devolvido', 'data_locacao')