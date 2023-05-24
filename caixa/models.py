from django.db import models


# Create your models here.
class Caixa(models.Model):
    TIPOS_TRANSACAO = (
        ('E', 'Entrada'),
        ('S', 'Saída')
    )
    data = models.DateField()
    tipo = models.CharField(max_length=1, choices=TIPOS_TRANSACAO)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.data} - {self.get_tipo_display()} - {self.descricao} - {self.valor}"

    def save(self, *args, **kwargs):
        if self.tipo == 'S':
            self.valor = self.valor * -1
        super(Caixa, self).save(*args, **kwargs)
