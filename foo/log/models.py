from django.db import models


class Log(models.Model):
    """
    A log table
    """
    name = models.CharField(max_length=30)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    info = models.CharField(max_length=300)

    class Admin:
        pass


