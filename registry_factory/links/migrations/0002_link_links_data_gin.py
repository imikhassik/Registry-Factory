# Generated by Django 4.2 on 2023-07-06 08:11

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='link',
            index=django.contrib.postgres.indexes.GinIndex(fields=['data'], name='links_data_gin'),
        ),
    ]
