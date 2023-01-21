from django.contrib import admin

from medicos.models import Especialidade, Medico, Agenda, Cliente


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']


class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'telefone',
    ]


class AgendaAdmin(admin.ModelAdmin):
    list_display = [
        'dia', 'medico', 'horario', 'cliente',
    ]


class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'telefone'
    ]


admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Agenda, AgendaAdmin)
