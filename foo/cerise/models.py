from django.db import models
from django_hstore import hstore


class Cerise(models.Model):
    """Simple model
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)
    data = hstore.DictionaryField(db_index=True, blank=True, null=True)
    objtxt = models.TextField()

    objects = hstore.HStoreManager()

    def __unicode__(self):
        return self.name
