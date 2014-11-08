from django.db import models

class Plum(models.Model):
    """
    """
    name = models.CharField(max_length=300)
    alphax = models.CharField(max_length=100, db_index=True)
    alphatx = models.CharField(max_length=100)
    alpha = models.CharField(max_length=100)
    resumex = models.TextField(db_index=True)
    resume = models.TextField()
