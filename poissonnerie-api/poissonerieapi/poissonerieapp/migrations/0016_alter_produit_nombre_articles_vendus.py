# Generated by Django 4.1.13 on 2024-03-17 22:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poissonerieapp", "0015_alter_produit_quantite_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produit",
            name="nombre_articles_vendus",
            field=models.IntegerField(default=0),
        ),
    ]
