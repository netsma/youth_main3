# Generated by Django 5.2.1 on 2025-06-04 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_rename_user_refreshtoken_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refreshtoken',
            old_name='user_id',
            new_name='user',
        ),
    ]
