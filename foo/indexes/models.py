from django.db import models
from django.contrib.sites.models import Site

# Create your models here.

class tem(models.Model):
    """
    A big table
    """
    method = models.CharField(max_length=10, default='unknown')
    name = models.CharField(max_length=300, db_index=True)


class BigItem(models.Model):
    """
    A big table
    """
    method = models.CharField(max_length=10, default='unknown')
    first_name = models.CharField(max_length=30, db_index=True)
    last_name = models.CharField(max_length=30, db_index=True)
    email = models.EmailField()
    email2 = models.EmailField()
    address = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    address3 = models.CharField(max_length=300)
    city_suffix = models.CharField(max_length=20, db_index=True)
    city = models.CharField(max_length=50, db_index=True)
    country1 = models.CharField(max_length=100)
    country2 = models.CharField(max_length=100, db_index=True)
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20, db_index=True)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    code1 = models.IntegerField()
    code2 = models.IntegerField()
    code3 = models.IntegerField()
    code4 = models.PositiveIntegerField()
    price1 = models.FloatField()
    price2 = models.FloatField()
    price3 = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
