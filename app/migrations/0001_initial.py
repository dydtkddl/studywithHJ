# Generated by Django 4.1.1 on 2023-04-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=2000, null=True)),
                ("content", models.TextField(null=True)),
                ("date", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
