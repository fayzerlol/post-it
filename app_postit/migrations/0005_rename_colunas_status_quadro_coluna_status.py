# Generated by Django 5.1 on 2024-11-21 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_postit", "0004_quadro_coluna_data_quadro_colunas_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quadro",
            old_name="colunas_status",
            new_name="coluna_status",
        ),
    ]
