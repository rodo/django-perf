from django.db import models

# Create your models here.

class Item(models.Model):
    """The client as consummer
    """
    method = models.CharField(max_length=10, default='unknown')
    name = models.CharField(max_length=300)
    datetms = models.FloatField()
    email = models.EmailField()
    value = models.FloatField()


class Company(models.Model):
    """
    A company
    """
    name = models.CharField(max_length=300, db_index=True)
    country = models.CharField(max_length=100, db_index=True)


class ComplexItem(models.Model):
    """The client as consummer
    """
    company = models.ForeignKey(Company)
    method = models.CharField(max_length=10, default='unknown')
    name = models.CharField(max_length=300, db_index=True)
    street_address = models.CharField(max_length=300)
    email = models.EmailField()
    value = models.FloatField()
    vali = models.FloatField(db_index=True)
    country = models.CharField(max_length=100, db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city_suffix = models.CharField(max_length=20, db_index=True)
    city = models.CharField(max_length=50, db_index=True)
    locale = models.CharField(max_length=8, db_index=True)

