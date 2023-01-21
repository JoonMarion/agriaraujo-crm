from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    path('registro/profissional/', views.medico_cadastro, name='medico_cadastro'),
    path('atualizar/profissional/<int:pk>', views.medico_atualizar, name='medico_atualizar'),
    path('apagar/profissional/<int:pk>', views.medico_deletar, name='medico_deletar'),

    path('registro/procedimento/', views.especialidade_cadastro, name='especialidade_cadastro'),
    path('atualizar/procedimento/<int:pk>', views.especialidade_atualizar, name='especialidade_atualizar'),
    path('apagar/procedimento/<int:pk>', views.especialidade_deletar, name='especialidade_deletar'),

    path('registro/cliente/', views.cliente_cadastro, name='cliente_cadastro'),
    path('atualizar/cliente/<int:pk>', views.cliente_atualizar, name='cliente_atualizar'),
    path('apagar/cliente/<int:pk>', views.cliente_deletar, name='cliente_deletar'),

    path('agendar/', views.agenda_cadastro, name='agendar_consulta'),
    path('agenda/atualizar/<int:pk>/', views.agenda_atualizar, name='agendar_consulta_atualizar'),
    path('agenda/apagar/<int:pk>/', views.agenda_deletar, name='agendar_consulta_deletar'),

    path('minhas/consultas/', views.agenda_lista, name="agenda_lista"),

    path('admin/lista/profissionais/', views.medico_lista, name="medicos_lista"),
    path('admin/lista/procedimentos/', views.especialidade_lista, name="especialidade_lista"),
    path('admin/lista/clientes/', views.cliente_lista, name="cliente_lista"),

]
