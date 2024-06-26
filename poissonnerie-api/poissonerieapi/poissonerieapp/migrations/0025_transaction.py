# Generated by Django 4.1.13 on 2024-03-18 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("poissonerieapp", "0024_kpi"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantite", models.IntegerField()),
                ("type_transaction", models.CharField(max_length=50)),
                (
                    "produit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="poissonerieapp.produit",
                    ),
                ),
            ],
        ),
    ]
