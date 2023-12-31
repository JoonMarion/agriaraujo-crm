# Generated by Django 4.0.1 on 2022-01-12 19:38

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Informe um nome de usuário válido. Este valor deve conter apenas letras, números e os carecteres: @/./+/-/_.', 'invalid')], verbose_name='Usuário'),
        ),
    ]
