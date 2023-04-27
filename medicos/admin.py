from django.contrib import admin

from medicos.models import Especialidade, Medico, Agenda, Cliente, Relatorio, Caixa


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']


class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'telefone',
    ]


class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'data', 'medico', 'horario', 'cliente', 'procedimento'
    ]


class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'telefone'
    ]


class RelatorioAdmin(admin.ModelAdmin):
    list_display = [
        'data', 'relatorio'
    ]


class CaixaAdmin(admin.ModelAdmin):
    list_display = [
        'data', 'tipo', 'descricao', 'valor'
    ]


admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Relatorio, RelatorioAdmin)
admin.site.register(Caixa, CaixaAdmin)
