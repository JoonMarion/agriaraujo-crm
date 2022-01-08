from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    path('registro/medico/', views.medico_cadastro, name='medico_cadastro'),
    path('registro/especialidade/', views.especialidade_cadastro, name='especialidade_cadastro'),
    path('agendar/', views.agenda_cadastro, name='agendar_consulta'),
    path('minhas/consultas/', views.agenda_lista, name="agenda_lista"),
    path('admim/lista/medicos/', views.medico_lista, name="medicos_lista"),
    path('admim/lista/especialidades/', views.especialidade_lista, name="especialidade_lista")
    
]