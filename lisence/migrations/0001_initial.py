# Generated by Django 4.2.4 on 2023-11-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lisence',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=100)),
                ('Activations', models.IntegerField()),
                ('Limit', models.IntegerField()),
            ],
        ),
    ]