# Generated by Django 4.1.7 on 2023-02-19 16:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_movie_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="tittle",
            new_name="title",
        ),
    ]
