# Generated by Django 4.1.4 on 2022-12-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_rename_categories_categorie"),
    ]

    operations = [
        migrations.AddField(
            model_name="categorie",
            name="studied",
            field=models.BooleanField(default=False),
        ),
    ]