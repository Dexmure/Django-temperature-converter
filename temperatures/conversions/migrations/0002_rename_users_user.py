# Generated by Django 5.1.3 on 2024-12-05 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='User',
        ),
    ]
