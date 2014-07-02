from django.db import models
from django.contrib.sites.models import Site


class Company(models.Model):
    """
    A big table
    """
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=30)

    
    class Admin:
        pass


class Orga(models.Model):
    """
    A big table
    """
    company = models.ForeignKey(Company)
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=30)


class Entry(models.Model):
    """
    A big table
    """
    site = models.ForeignKey(Site)
    name = models.CharField(max_length=30)
    companies = models.ManyToManyField(Company, blank=True)
    orgas = models.ManyToManyField(Orga, blank=True)
