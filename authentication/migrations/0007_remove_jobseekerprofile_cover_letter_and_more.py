# Generated by Django 4.1.7 on 2023-04-05 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_jobseekerprofile_citizenship_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='cover_letter',
        ),
        migrations.RemoveField(
            model_name='jobseekerprofile',
            name='resume',
        ),
    ]
