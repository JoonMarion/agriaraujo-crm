# Generated by Django 4.0.1 on 2023-01-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0007_alter_agenda_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='cliente',
            field=models.CharField(max_length=200, verbose_name='Cliente'),
        ),
    ]
