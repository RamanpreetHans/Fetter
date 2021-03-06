# Generated by Django 2.1.2 on 2018-11-04 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0009_auto_20181103_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='intended_for',
            field=models.CharField(choices=[('students', 'Students'), ('faculty_and_professors', 'Faculty_and_Professors'), ('all', 'All')], default='all', max_length=50),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
