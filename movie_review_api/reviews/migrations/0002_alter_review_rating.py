# Generated by Django 5.1.2 on 2024-10-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveIntegerField(),
        ),
    ]
