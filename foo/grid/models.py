from django.db import models
from djorm_pgarray.fields import TextArrayField
from djorm_pgarray.fields import IntegerArrayField
from djorm_expressions.models import ExpressionManager
from django_hstore import hstore
"""
Find a grid depending on his tag

"""

class Grid(models.Model):
    """Array field with integer"""
    name = models.CharField(max_length=300)
    alpha = models.CharField(max_length=30)
    old = models.TextField(db_index=True)
    tags = IntegerArrayField(db_index=True)

    objects = ExpressionManager()

class Grad(models.Model):
    """Array field with varchar"""
    name = models.CharField(max_length=300)
    alpha = models.CharField(max_length=30)
    old = models.TextField()
    tags = TextArrayField()

    objects = ExpressionManager()

class GridForeign(models.Model):
    """What is a Grod"""
    grid_id = models.IntegerField()
    tag = models.IntegerField(db_index=True)
