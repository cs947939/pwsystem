# Generated by Django 4.2.4 on 2023-08-03 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pwmanager", "0011_delete_pwuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="encryption",
            name="Id",
        ),
        migrations.RemoveField(
            model_name="password",
            name="Owner",
        ),
        migrations.RemoveField(
            model_name="password",
            name="id",
        ),
        migrations.RemoveField(
            model_name="secret",
            name="Key_ID",
        ),
        migrations.RemoveField(
            model_name="secret",
            name="id",
        ),
        migrations.AddField(
            model_name="password",
            name="Note",
            field=models.CharField(blank=True, default="this is blank", max_length=500),
        ),
        migrations.AddField(
            model_name="password",
            name="URL",
            field=models.URLField(blank=True, default="google.com"),
        ),
        migrations.AlterField(
            model_name="encryption",
            name="Salt",
            field=models.CharField(default="0", max_length=500),
        ),
        migrations.AlterField(
            model_name="password",
            name="Date_Created",
            field=models.DateField(default=datetime.date(2023, 8, 3)),
        ),
        migrations.AlterField(
            model_name="password",
            name="Id",
            field=models.IntegerField(
                blank=True,
                default="0000",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AddField(
            model_name="secret",
            name="Id",
            field=models.IntegerField(
                blank=True,
                default="0000",
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]