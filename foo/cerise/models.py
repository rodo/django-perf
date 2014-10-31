from django.db import models
from django_hstore import hstore


class Apple(models.Model):
    """The client as consummer
    """
    name = models.CharField(max_length=300)
    data = hstore.DictionaryField(db_index=True)
    objects = hstore.HStoreManager()

    def __unicode__(self):
        return self.name
