# Generated by Django 4.2.13 on 2024-05-10 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "StudenHelp",
            "0004_reaction_comment_reaction_like_user_email_user_nom_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="poste",
            old_name="users",
            new_name="uc",
        ),
    ]