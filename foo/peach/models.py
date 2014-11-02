from django.db import models


class Small(models.Model):
    """A small table
    """
    name = models.CharField(max_length=300)
    data = hstore.DictionaryField(db_index=True)
    indice = models.IntegerField(default=0)
    objects = hstore.HStoreManager()

    def __unicode__(self):
        return self.name
