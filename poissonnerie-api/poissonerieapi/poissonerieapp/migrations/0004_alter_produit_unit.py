# Generated by Django 4.1.13 on 2024-03-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poissonerieapp", "0003_alter_produit_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produit",
            name="unit",
            field=models.CharField(default="Kg", max_length=10),
        ),
    ]