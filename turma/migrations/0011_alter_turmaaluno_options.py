# Generated by Django 4.2.18 on 2025-03-02 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0010_alter_turmaaluno_matricula_aluno_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turmaaluno',
            options={'ordering': ['numero_turma', 'matricula_aluno']},
        ),
    ]
