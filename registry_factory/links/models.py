import uuid

from django.contrib.postgres.indexes import GinIndex
from django.db import models, connection
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver


def get_next_internal_id():
    with connection.cursor() as cursor:
        cursor.execute("CREATE SEQUENCE IF NOT EXISTS links_internal_id_seq START WITH 1 INCREMENT BY 1")
        cursor.execute("SELECT nextval('links_internal_id_seq')")
        result = cursor.fetchone()
        return result[0]


def meta_default_value(internal_id_placeholder=None):
    return {
        "status": "active",
        "flags": 0,
        "internal_id": internal_id_placeholder
    }


class Link(models.Model):

    DIRECTION_CHOICES = [
        (0, '00'),
        (1, '01'),
        (2, '10'),
        (3, '11'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    link_type = models.CharField(max_length=254)
    object1 = models.UUIDField()
    object2 = models.UUIDField()
    weight = models.FloatField(validators=[MinValueValidator(0.0),
                                           MaxValueValidator(1.0)],
                               default=0.0)
    direction = models.SmallIntegerField(choices=DIRECTION_CHOICES,
                                         validators=[MinValueValidator(0),
                                                     MaxValueValidator(3)],
                                         default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    meta = models.JSONField(default=meta_default_value)
    data = models.JSONField(null=True)
    project_id = models.UUIDField(default=None, null=True)
    account_id = models.UUIDField(default=None, null=True)
    user_id = models.UUIDField(default=None, null=True)

    class Meta:
        constraints = (
            models.CheckConstraint(
                check=models.Q(weight__gte=0.0) & models.Q(weight__lte=1.0),
                name='link_weight_range'),
            models.CheckConstraint(
                check=models.Q(direction__gte=0) & models.Q(direction__lte=3),
                name='link_direction_range'
            )
        )
        indexes = [
            GinIndex(fields=['data'], name='links_data_gin'),
        ]
        ordering = ['-meta__internal_id']


@receiver(pre_save, sender=Link)
def set_meta(sender, instance, **kwargs):
    try:
        Link.objects.get(id=instance.id)
    except Link.DoesNotExist:
        if 'status' not in instance.meta.keys():
            instance.meta['status'] = "active"
        if 'flags' not in instance.meta.keys():
            instance.meta['flags'] = 0
        instance.meta['internal_id'] = get_next_internal_id()
