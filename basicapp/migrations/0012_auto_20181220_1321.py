# Generated by Django 2.1.2 on 2018-12-20 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicapp', '0011_auto_20181218_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='basicapp.Interests')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='intersts',
            name='user_name',
        ),
        migrations.RenameField(
            model_name='societies',
            old_name='instite_name',
            new_name='institute_name',
        ),
        migrations.DeleteModel(
            name='Intersts',
        ),
    ]
