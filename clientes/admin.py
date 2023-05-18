from django.contrib import admin
from clientes.models import Cliente, Transacao


class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'telefone'
    ]


class TransacaoAdmin(admin.ModelAdmin):
    list_display = [
        'cliente', 'data', 'descricao', 'quantidade_kg', 'tipo'
    ]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Transacao, TransacaoAdmin)
