# Generated by Django 4.2.5 on 2023-09-20 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("plants_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="plant",
            old_name="areas_in_Uganda",
            new_name="regions",
        ),
        migrations.RemoveField(
            model_name="plant",
            name="medicinal_use",
        ),
        migrations.CreateModel(
            name="Medicinal_Plant",
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
                (
                    "medicinal_use",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="plants_app.medicinal_use",
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="plants_app.plant",
                    ),
                ),
            ],
        ),
    ]
