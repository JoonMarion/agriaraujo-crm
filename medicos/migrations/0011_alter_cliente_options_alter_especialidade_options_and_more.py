# Generated by Django 4.0.1 on 2023-04-13 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0010_remove_medico_especialidade_agenda_procedimento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='especialidade',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='medico',
            options={'ordering': ['nome']},
        ),
        migrations.AddField(
            model_name='cliente',
            name='avaliacao',
            field=models.TextField(blank=True, null=True, verbose_name='Avaliação'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='procedimento',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='medicos.especialidade', verbose_name='Procedimento'),
        ),
    ]
