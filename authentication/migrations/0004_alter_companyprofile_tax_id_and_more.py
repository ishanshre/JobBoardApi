# Generated by Django 4.1.7 on 2023-03-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_companyprofile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='tax_id',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='tax_id',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
