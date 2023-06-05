from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator
from django.forms import TextInput
from .utils import calcular_valor_total


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    anotacoes = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.nome


class Transacao(models.Model):
    TIPOS_TRANSACAO = (
        ('E', 'Entrada'),
        ('S', 'Saída')
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    quantidade_kg = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    valor_kg = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPOS_TRANSACAO)
    valor_total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.descricao + ' - ' + self.cliente.nome + ' - ' + str(self.data)

    def save(self, *args, **kwargs):
        self.quantidade_kg, self.valor_kg, self.valor_total = calcular_valor_total(
            self.tipo, self.quantidade_kg, self.valor_kg, self.valor_total
        )
        super().save(*args, **kwargs)

