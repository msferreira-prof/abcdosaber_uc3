# Generated by Django 4.2.18 on 2025-02-12 23:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_alter_aluno_options_alter_aluno_data_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 12, 23, 51, 11, 758970, tzinfo=datetime.timezone.utc), help_text='Informe a data inicial de matrícula do Aluno'),
        ),
    ]
