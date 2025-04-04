# Generated by Django 4.2.18 on 2025-03-03 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0015_alter_aluno_data_inicial'),
        ('turma', '0013_alter_ausencia_options_alter_turmaaluno_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmaaluno',
            name='matricula_aluno',
            field=models.ForeignKey(help_text='Matrícula do aluno da turma', on_delete=django.db.models.deletion.CASCADE, related_name='alunos_turmas', to='aluno.aluno'),
        ),
    ]
