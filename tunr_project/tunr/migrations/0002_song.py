# Generated by Django 4.1.7 on 2023-03-29 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tunr", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("title", models.CharField(default="no song title", max_length=100)),
                ("album", models.CharField(default="no album title", max_length=100)),
                ("preview_url", models.CharField(max_length=200, null=True)),
                (
                    "artists",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="songs",
                        to="tunr.artist",
                    ),
                ),
            ],
        ),
    ]
