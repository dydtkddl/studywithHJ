# Generated by Django 4.1.6 on 2023-04-05 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_article_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="user_id",
            new_name="user",
        ),
    ]
