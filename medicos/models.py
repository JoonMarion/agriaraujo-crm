from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey


class Especialidade(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    
    def __str__(self):
        return f'{self.nome}'


class Medico(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    email = models.EmailField(verbose_name="Email")
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número precisa estar neste formato: \
                    '91988887777'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    especialidade = ForeignKey(Especialidade,
                               on_delete=models.CASCADE,
                               related_name='medicos')
    
    def __str__(self):
        return f'{self.nome}'


def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')


class Agenda(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda', verbose_name='Especialista')
    dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])
    
    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
        ("6", "12:00 ás 13:00"),
        ("7", "13:00 ás 14:00"),
        ("8", "14:00 ás 15:00"),
        ("9", "15:00 ás 16:00"),
        ("10", "16:00 ás 17:00"),
        ("11", "17:00 ás 18:00"),
    )

    horario = models.CharField(max_length=10, choices=HORARIOS, verbose_name='Horário')
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário', 
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('horario', 'dia')
        
    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.medico}'
