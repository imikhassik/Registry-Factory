# Generated by Django 4.2 on 2023-08-01 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_link_links_data_gin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-meta__internal_id']},
        ),
    ]