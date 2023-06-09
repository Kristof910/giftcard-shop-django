# Generated by Django 4.2 on 2023-04-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_website", "0004_giftcard_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="giftcardregion",
            name="currency_symbol",
            field=models.CharField(default="€", max_length=1),
        ),
        migrations.AlterField(
            model_name="giftcardregion",
            name="name",
            field=models.CharField(default="Europe", max_length=30),
        ),
        migrations.AlterField(
            model_name="giftcardtype",
            name="description",
            field=models.TextField(
                blank=True,
                default="This is a description for Apple Giftcard.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="giftcardtype",
            name="name",
            field=models.CharField(default="Apple", max_length=50),
        ),
        migrations.AlterField(
            model_name="giftcardvalue",
            name="value",
            field=models.PositiveIntegerField(default=10),
        ),
    ]
