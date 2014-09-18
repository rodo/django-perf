from django.db import models

# Create your models here.

class Log(models.Model):
    """
    A log table
    """
    name = models.CharField(max_length=30)
    start = models.DateTimeField()
    stop = models.DateTimeField()


    class Admin:
        pass


