# Generated by Django 4.2.18 on 2025-02-14 23:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0013_alter_aluno_data_inicial'),
        ('turma', '0004_remove_turma_codigo_titulo_turma_id_instrutor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='data_final',
            field=models.DateField(default=datetime.datetime(2025, 2, 14, 23, 21, 4, 817383, tzinfo=datetime.timezone.utc), help_text='Informe a data final da Turma'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_inicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 14, 23, 21, 4, 816390, tzinfo=datetime.timezone.utc), help_text='Informe a data inicial da Turma'),
        ),
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio_matricula', models.DateField(default=datetime.datetime(2025, 2, 14, 23, 21, 4, 817383, tzinfo=datetime.timezone.utc), help_text='Data da matrícula do aluno na turma')),
                ('data_fim_matricula', models.DateField(blank=True, help_text='Data de fim de matrícula do aluno na turma', null=True)),
                ('matricula_aluno', models.ForeignKey(help_text='Matrícula do aluno da turma', on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('numero_turma', models.ForeignKey(help_text='Número da turma do aluno.', on_delete=django.db.models.deletion.CASCADE, to='turma.turma')),
            ],
        ),
    ]
