# Generated by Django 4.1.7 on 2023-02-19 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("tittle", models.CharField(max_length=127)),
                ("duration", models.CharField(max_length=10, null=True)),
                ("synopsis", models.TextField(null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("PG", "Pg"),
                            ("PG-13", "Pg 13"),
                            ("R", "R R"),
                            ("NC-17", "Nc 17"),
                            ("G", "Default"),
                        ],
                        default="G",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]