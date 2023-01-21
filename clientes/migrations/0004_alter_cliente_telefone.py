# Generated by Django 4.0.1 on 2023-01-21 05:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="O número precisa estar neste formato:                         '91988887777'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefone'),
        ),
    ]