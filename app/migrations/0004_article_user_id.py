# Generated by Django 4.1.6 on 2023-04-05 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_rename_nickname_user_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="user_id",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.user"
            ),
        ),
    ]