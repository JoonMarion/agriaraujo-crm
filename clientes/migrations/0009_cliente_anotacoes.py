# Generated by Django 4.0.1 on 2023-05-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_cliente_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='anotacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
