from django.db import models, connection
from django_hstore import hstore
 
# Create your models here.

class Preferences(models.Model):
    """The client as consummer
    """
    name = models.CharField(max_length=300)
    data = hstore.DictionaryField(db_index=True)
    objects = hstore.HStoreManager()

    def __unicode__(self):
        return self.name

class Company(models.Model):
    """The client as consummer
    """
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=300)

class Organisation(models.Model):
    """The client as consummer
    """
    name = models.CharField(max_length=300)


class Client(models.Model):
    """The client as consummer
    """
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    firstname = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    addr2 = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    lastlogin = models.DateField()
    users = models.PositiveIntegerField()
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Customer(Client):
    """
    Based on the view bar_customer
    """
    class Meta:
        managed = False

