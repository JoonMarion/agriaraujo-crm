from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey


class Especialidade(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}'


class Medico(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número precisa estar neste formato: \
                    '91988887777'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}'


class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número precisa estar neste formato: \
                        '91988887777'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)

    avaliacao = models.TextField(verbose_name="Avaliação", null=True, blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome}'


def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')


class Agenda(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda', verbose_name='Profissional')

    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agenda', verbose_name='Cliente')

    data = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])

    procedimento = models.ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='agenda', verbose_name='Procedimento', default=None)

    horario = models.CharField(verbose_name="Horário", max_length=30, default=None)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('horario', 'data')

    def __str__(self):
        return f'{self.data.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.medico} - {self.cliente}'


class Relatorio(models.Model):

    relatorio = models.TextField(verbose_name="Relatório", null=True, blank=True)
    data = models.DateField(help_text="Insira uma data para agenda", null=True, blank=True)

    def __str__(self):
        return f'{self.data.strftime("%b %d %Y")}'
