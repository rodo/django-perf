from __future__ import absolute_import

from celery import shared_task
from foo.loader.models import Item
from foo.loader.utils import dobulk
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

@shared_task
def bulkinsert(self, values, nb):
    """
    Save values in DB
    """
    i = 0
    nbval = len(values)
    part = int(round(nbval / nb))

    while i < nb:
        poms = []
        low = i * part
        high = low + part
        dobulk(values, low, high)
        i = i + 1 

    if high < nbval:
        dobulk(values, high, nbval)
