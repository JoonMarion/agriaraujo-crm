from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('lista/produtor/', views.cliente_lista, name="cliente_lista"),
    path('cadastro/produtor/', views.cliente_cadastro, name="cliente_cadastro"),
    path('atualizar/produtor/<int:pk>/', views.cliente_atualizar, name="cliente_atualizar"),
    path('deletar/produtor/<int:pk>/', views.cliente_deletar, name="cliente_deletar"),

    path('lista/transacao/<int:pk>/', views.transacao_lista, name="transacao_lista"),
    path('cadastro/transacao/<int:pk>/', views.transacao_cadastro, name="transacao_cadastro"),
    path('atualizar/transacao/<int:pk>/', views.transacao_atualizar, name="transacao_atualizar"),
    path('deletar/transacao/<int:pk>/', views.transacao_deletar, name="transacao_deletar"),

    path('imprimir/<int:transacao_id>/', views.transacao_imprimir, name='transacao_imprimir'),
    path('download-xlsx/<int:cliente_id>/', views.download_xlsx, name='download_xlsx'),
]
