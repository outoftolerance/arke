# Generated by Django 3.1.2 on 2020-10-08 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Received',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(default='', max_length=16, validators=[django.core.validators.MinLengthValidator(15)])),
                ('sequence_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)])),
                ('timestamp_transmit', models.DateTimeField()),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('circular_error_probable', models.DecimalField(decimal_places=4, max_digits=12)),
                ('data', models.TextField(verbose_name=2048)),
            ],
        ),
    ]