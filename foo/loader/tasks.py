from __future__ import absolute_import

from celery import shared_task
from foo.loader.models import Item
import time

@shared_task
def mul(x, y):
    return x * y

@shared_task
def insert(values):
    """
    Save values in DB
    """
    for val in values:
        Item.objects.create(datetms=val['datetms'],
                            name=val['name'],
                            email=val['email'],
                            value=val['value'])

