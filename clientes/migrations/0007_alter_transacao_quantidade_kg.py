# Generated by Django 4.0.1 on 2023-05-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_rename_valor_transacao_valor_kg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='quantidade_kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]