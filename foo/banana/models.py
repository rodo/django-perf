from django.db import models

class Owner(models.Model):
    """
    """
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=30)

class Fruit(models.Model):
    """
    """
    family = models.CharField(max_length=300)
    beta = models.CharField(max_length=30)

class Variety(models.Model):
    """
    """
    name = models.CharField(max_length=300)
    beta = models.CharField(max_length=30)
    code = models.IntegerField(default=400)
    owner = models.ForeignKey(Owner)

class Color(models.Model):
    """
    """
    name = models.CharField(max_length=300)
    code = models.IntegerField()
    epsilon = models.CharField(max_length=30)


class Banana(models.Model):
    """An apple
    """
    name = models.CharField(max_length=300)
    alpha = models.CharField(max_length=30)
    code = models.IntegerField()
    color = models.ForeignKey(Color)
    fruit = models.ForeignKey(Fruit)
    variety = models.ForeignKey(Variety)

    def __unicode__(self):
        return self.name
