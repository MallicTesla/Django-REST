# Generated by Django 4.2.5 on 2023-10-20 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_rename_es_activo_historicalusuario_is_active_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalUsuario',
        ),
    ]