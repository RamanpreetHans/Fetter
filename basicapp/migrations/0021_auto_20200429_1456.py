# Generated by Django 3.0.2 on 2020-04-29 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0020_auto_20200429_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_table',
            old_name='profile_pic',
            new_name='profile_pic_path',
        ),
    ]