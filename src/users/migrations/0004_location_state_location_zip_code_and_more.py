# Generated by Django 5.1.2 on 2024-10-30 09:41

import localflavor.us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.us.models.USStateField(default='NY', max_length=2),
        ),
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
