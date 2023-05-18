from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('lista/cliente/', views.cliente_lista, name="cliente_lista"),
    path('cadastro/cliente/', views.cliente_cadastro, name="cliente_cadastro"),
    path('atualizar/cliente/<int:pk>/', views.cliente_atualizar, name="cliente_atualizar"),
    path('deletar/cliente/<int:pk>/', views.cliente_deletar, name="cliente_deletar"),

    path('lista/transacao/<int:pk>/', views.transacao_lista, name="transacao_lista"),
    path('cadastro/transacao/<int:pk>/', views.transacao_cadastro, name="transacao_cadastro"),
    path('atualizar/transacao/<int:pk>/', views.transacao_atualizar, name="transacao_atualizar"),
    path('deletar/transacao/<int:pk>/', views.transacao_deletar, name="transacao_deletar"),
]
