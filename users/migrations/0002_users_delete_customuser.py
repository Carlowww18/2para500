# Generated by Django 5.1.3 on 2024-11-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="users",
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
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "Administrador"),
                            ("manager", "Gerente"),
                            ("seller", "Cambista"),
                            ("client", "Cliente"),
                        ],
                        max_length=10,
                    ),
                ),
                ("cidade", models.CharField(blank=True, max_length=100, null=True)),
                ("username", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
