# Generated by Django 4.2 on 2023-05-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_website", "0009_alter_giftcardvalue_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingCost",
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
                ("cost", models.PositiveIntegerField(default=10)),
            ],
        ),
    ]