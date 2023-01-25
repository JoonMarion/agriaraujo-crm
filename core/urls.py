from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from medicos.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('clientes/', include('clientes.urls', namespace="clientes")),
    path('main/', include('medicos.urls', namespace="medicos")),
]
