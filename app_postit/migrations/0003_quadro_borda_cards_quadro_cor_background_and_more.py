# Generated by Django 5.1 on 2024-08-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_postit", "0002_alter_card_conteudo_alter_card_detalhes"),
    ]

    operations = [
        migrations.AddField(
            model_name="quadro",
            name="borda_cards",
            field=models.CharField(
                blank=True, default="#000000", max_length=7, null=True
            ),
        ),
        migrations.AddField(
            model_name="quadro",
            name="cor_background",
            field=models.CharField(
                blank=True, default="#ffffff", max_length=7, null=True
            ),
        ),
        migrations.AddField(
            model_name="quadro",
            name="cor_cards",
            field=models.CharField(
                blank=True, default="#f8f9fa", max_length=7, null=True
            ),
        ),
        migrations.AddField(
            model_name="quadro",
            name="cor_fonte",
            field=models.CharField(
                blank=True, default="#000000", max_length=7, null=True
            ),
        ),
        migrations.AddField(
            model_name="quadro",
            name="sombra_cards",
            field=models.CharField(
                blank=True,
                default="0px 0px 10px rgba(0, 0, 0, 0.1)",
                max_length=7,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="quadro",
            name="tamanho_fonte",
            field=models.CharField(
                blank=True, default="16px", max_length=10, null=True
            ),
        ),
    ]
