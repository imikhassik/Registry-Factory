import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_object_item'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='Company'.lower(),
            index=django.contrib.postgres.indexes.GinIndex(fields=['data'], name='companies_data_gin'),
        ),
        migrations.AddIndex(
            model_name='Company'.lower(),
            index=models.Index(fields=['object_item'], name='companies_object_item_idx'),
        ),
    ]
