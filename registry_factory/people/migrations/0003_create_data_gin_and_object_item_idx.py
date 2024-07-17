import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_alter_object_item'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='Person'.lower(),
            index=django.contrib.postgres.indexes.GinIndex(fields=['data'], name='people_data_gin'),
        ),
        migrations.AddIndex(
            model_name='Person'.lower(),
            index=models.Index(fields=['object_item'], name='people_object_item_idx'),
        ),
    ]
