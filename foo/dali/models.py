from django.db import models

class Fishon(models.Model):
    """A Fish"""
    name = models.CharField(max_length=300)
    alpha = models.CharField(max_length=30)


class Fish(models.Model):
    """A Fish"""
    name = models.CharField(max_length=300)
    alpha = models.CharField(max_length=30)
    code = models.IntegerField()
    fishon = models.ManyToManyField(Fishon)

    class Meta:
        ordering = ['pk']

    def __unicode__(self):
        return self.name
