# Generated by Django 4.2 on 2023-05-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_website", "0014_rename_contactmessages_contactmessage_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="giftcardcode",
            name="status",
            field=models.BooleanField(
                default=True, help_text="If this is not active, it means it was sold!"
            ),
        ),
    ]
