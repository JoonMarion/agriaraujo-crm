# Generated by Django 4.0.1 on 2023-04-13 06:36

from django.db import migrations, models
import medicos.models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0013_relatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='dia',
            field=models.DateField(blank=True, help_text='Insira a data', null=True, validators=[medicos.models.validar_dia]),
        ),
    ]
