import uuid

from django.contrib.postgres.indexes import GinIndex
from django.db import models, connection
from django.db.models.signals import pre_save
from django.dispatch import receiver


def get_next_internal_id():
    with connection.cursor() as cursor:
        cursor.execute("CREATE SEQUENCE IF NOT EXISTS companies_internal_id_seq START WITH 1 INCREMENT BY 1")
        cursor.execute("SELECT nextval('companies_internal_id_seq')")
        result = cursor.fetchone()
        return result[0]


def meta_default_value(internal_id_placeholder=None):
    return {
        "status": "active",
        "flags": 0,
        "internal_id": internal_id_placeholder
    }


class Company(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    object_type = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    object_code = models.CharField(max_length=254)  # e.g. phone # or email for a contact
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    meta = models.JSONField(default=meta_default_value)
    data = models.JSONField(null=True)
    project_id = models.UUIDField(default=None, null=True)
    account_id = models.UUIDField(default=None, null=True)
    user_id = models.UUIDField(default=None, null=True)
    object_item = models.UUIDField(default=None, null=True)  # e.g. attachment to a Task object

    class Meta:
        indexes = [
            GinIndex(fields=['data'], name='companies_data_gin'),
            models.Index(fields=['object_item'], name='companies_object_item_idx'),
        ]
        ordering = ['-meta__internal_id']


@receiver(pre_save, sender=Company)
def set_meta(sender, instance, **kwargs):
    try:
        Company.objects.get(id=instance.id)
    except Company.DoesNotExist:
        if 'status' not in instance.meta.keys():
            instance.meta['status'] = "active"
        if 'flags' not in instance.meta.keys():
            instance.meta['flags'] = 0
        instance.meta['internal_id'] = get_next_internal_id()
