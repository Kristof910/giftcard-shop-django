# Generated by Django 4.2 on 2023-05-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_website", "0010_shippingcost"),
    ]

    operations = [
        migrations.AddField(
            model_name="shippingcost",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]
