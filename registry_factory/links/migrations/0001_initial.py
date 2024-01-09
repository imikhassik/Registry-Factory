# Generated by Django 4.2 on 2023-06-21 07:42

import django.core.validators
from django.db import migrations, models
import links.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link_type', models.CharField(max_length=254)),
                ('object1', models.UUIDField()),
                ('object2', models.UUIDField()),
                ('weight', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('direction', models.SmallIntegerField(choices=[(0, '00'), (1, '01'), (2, '10'), (3, '11')], default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('meta', models.JSONField(default=links.models.meta_default_value)),
                ('data', models.JSONField(null=True)),
                ('project_id', models.UUIDField(default=None, null=True)),
                ('account_id', models.UUIDField(default=None, null=True)),
                ('user_id', models.UUIDField(default=None, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='link',
            constraint=models.CheckConstraint(check=models.Q(('weight__gte', 0.0), ('weight__lte', 1.0)), name='link_weight_range'),
        ),
        migrations.AddConstraint(
            model_name='link',
            constraint=models.CheckConstraint(check=models.Q(('direction__gte', 0), ('direction__lte', 3)), name='link_direction_range'),
        ),
    ]