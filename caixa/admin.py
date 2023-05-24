from django.contrib import admin
from caixa.models import Caixa


class CaixaAdmin(admin.ModelAdmin):
    list_display = [
        'data', 'tipo', 'descricao', 'valor'
    ]


admin.site.register(Caixa, CaixaAdmin)

