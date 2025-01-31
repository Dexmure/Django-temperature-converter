# Generated by Django 5.1.3 on 2024-12-04 20:47

import conversions.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='historic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('val_initial', models.FloatField()),
                ('val_final', models.FloatField()),
                ('initial_conv', models.CharField(choices=[('C', 'CELSIUS'), ('F', 'FAHRENHEIT')], max_length=1, validators=[conversions.models.validate_choice])),
                ('final_conv', models.CharField(choices=[('C', 'CELSIUS'), ('F', 'FAHRENHEIT')], max_length=1, validators=[conversions.models.validate_choice])),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conversions.users')),
            ],
        ),
    ]
