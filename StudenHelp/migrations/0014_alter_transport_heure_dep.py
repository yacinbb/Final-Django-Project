# Generated by Django 4.2.13 on 2024-05-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("StudenHelp", "0013_alter_transport_heure_dep"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transport",
            name="heure_dep",
            field=models.TimeField(),
        ),
    ]
