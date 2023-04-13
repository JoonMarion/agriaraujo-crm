# Generated by Django 4.0.1 on 2023-04-13 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0018_rename_data_relatorio_dia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='dia',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='relatorio',
            old_name='dia',
            new_name='data',
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('horario', 'data')},
        ),
    ]
