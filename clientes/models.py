from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator
from django.forms import TextInput


class Cliente(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O número precisa estar neste formato: \'91988887777'.")
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True, blank=True, validators=[phone_regex])

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
        if self.tipo == 'S' and self.quantidade_kg:
            self.quantidade_kg = -self.quantidade_kg

        if self.valor_kg and self.quantidade_kg:
            if self.tipo == 'S':
                self.valor_total = -Decimal(self.quantidade_kg) * Decimal(self.valor_kg)
            else:
                self.valor_total = Decimal(self.quantidade_kg) * Decimal(self.valor_kg)
        elif self.valor_kg and self.valor_total:
            if self.tipo == 'S':
                self.quantidade_kg = -Decimal(self.valor_total) / Decimal(self.valor_kg)
            else:
                self.quantidade_kg = Decimal(self.valor_total) / Decimal(self.valor_kg)
        elif self.quantidade_kg and self.valor_total:
            if self.tipo == 'S':
                self.valor_kg = -Decimal(self.valor_total) / Decimal(self.quantidade_kg)
            else:
                self.valor_kg = Decimal(self.valor_total) / Decimal(self.quantidade_kg)
        super(Transacao, self).save(*args, **kwargs)

