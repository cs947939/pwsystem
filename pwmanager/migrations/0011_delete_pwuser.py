# Generated by Django 4.2.4 on 2023-08-03 14:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pwmanager", "0010_pwuser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PwUser",
        ),
    ]
