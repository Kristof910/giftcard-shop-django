# Generated by Django 4.2 on 2023-04-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GiftcardRegion",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="GiftcardType",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GiftcardValue",
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
                ("name", models.CharField(max_length=10)),
                ("value", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Giftcard",
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
                ("is_digital", models.BooleanField(default=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("available_stock", models.PositiveIntegerField()),
                ("region", models.ManyToManyField(to="main_website.giftcardregion")),
                ("type", models.ManyToManyField(to="main_website.giftcardtype")),
                ("value", models.ManyToManyField(to="main_website.giftcardvalue")),
            ],
        ),
    ]