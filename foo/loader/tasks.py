from __future__ import absolute_import

from celery import shared_task
from foo.loader.models import Item
from foo.loader.utils import dobulk
import time
import os
from uuid import uuid4
from django.db import connection


@shared_task
def mul(x, y):
    return x * y

@shared_task
def insert(values):
    """
    Save values in DB
    """
    for val in values:
        res = Item.objects.create(method="sequential",
                                  datetms=val['datetms'],
                                  name=val['name'],
                                  email=val['email'],
                                  value=val['value'])

@shared_task
def bulkinsert(values, method):
    """
    Save values in DB

    nb (integer): number of part to split the values on
    """
    dobulk(values, method, low, high)

@shared_task
def copyinsert(values, method):
    """
    Use COPY to insert datas
    """
    fields = ['datetms', 'name', 'email', 'value', 'method']

    fpath = os.path.join('/tmp/', str(uuid4()))
    f = open(fpath, 'w')
    for val in values:
        f.write('{},"{}","{}",{},{}\n'.format(val['datetms'],
                                                val['name'],
                                                val['email'],
                                                val['value'],
                                                method))
    f.close()
    cursor = connection.cursor()
    cursor.copy_from(open(fpath, 'r'), 'loader_item', columns=tuple(fields), sep=',')
    unlink(fpath)
