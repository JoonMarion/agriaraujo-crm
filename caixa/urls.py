from django.urls import path
from . import views

app_name = 'caixa'

urlpatterns = [
    path('admin/lista/', views.caixa_lista, name="caixa_lista"),
    path('registro/', views.caixa_cadastro, name='caixa_cadastro'),
    path('atualizar/<int:pk>', views.caixa_atualizar, name='caixa_atualizar'),
    path('apagar/<int:pk>', views.caixa_deletar, name='caixa_deletar'),

    path('download_xlsx/', views.download_xlsx, name='download_xlsx'),
    path('imprimir/<int:caixa_id>/', views.caixa_imprimir, name='caixa_imprimir'),
]
