from django.contrib import admin
from caixa.models import Caixa


class CaixaAdmin(admin.ModelAdmin):
    list_display = [
        'data', 'descricao', 'quantidade_kg', 'valor_kg', 'tipo', 'valor_total'
    ]

admin.site.register(Caixa, CaixaAdmin)

