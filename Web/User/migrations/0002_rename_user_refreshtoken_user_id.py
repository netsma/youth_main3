# Generated by Django 5.2.1 on 2025-06-04 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refreshtoken',
            old_name='user',
            new_name='user_id',
        ),
    ]
