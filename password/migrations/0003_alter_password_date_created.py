# Generated by Django 4.1.6 on 2023-02-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("password", "0002_password_atachment_password_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="password",
            name="Date_Created",
            field=models.DateField(default="2023-02-01"),
        ),
    ]