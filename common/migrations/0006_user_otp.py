# Generated by Django 4.1.5 on 2023-05-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0005_appliedjobs_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="otp",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
