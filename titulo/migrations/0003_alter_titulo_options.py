# Generated by Django 4.2.18 on 2025-03-03 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titulo', '0002_alter_titulo_codigo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titulo',
            options={'ordering': ['codigo']},
        ),
    ]
