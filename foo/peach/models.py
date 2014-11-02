from django.db import models


class Small(models.Model):
    """A small table
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Tiny(models.Model):
    """A small table
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Big(models.Model):
    """A small table
    """
    name = models.CharField(max_length=300)
    indice = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name
