from django.db import models
import reversion

class Item(models.Model):
    """The client as consummer
    """
    name = models.CharField(max_length=300)
    value = models.FloatField()

reversion.register(Item)
