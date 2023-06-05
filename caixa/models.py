from django.db import models
from decimal import Decimal
from clientes.utils import calcular_valor_total


# Create your models here.
class Caixa(models.Model):
    TIPOS_TRANSACAO = (
        ('E', 'Entrada'),
    )
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    quantidade_kg = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=TIPOS_TRANSACAO, default='E')
    valor_total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    valor_kg = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.descricao + ' - ' + self.cliente.nome + ' - ' + str(self.data)

    def save(self, *args, **kwargs):
        self.quantidade_kg, self.valor_kg, self.valor_total = calcular_valor_total(
            self.tipo, self.quantidade_kg, self.valor_kg, self.valor_total
        )
        super().save(*args, **kwargs)
