from django.db import models

class Editor(models.Model):
    """
    """
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=150)

class Company(models.Model):
    """
    """
    family = models.CharField(max_length=300)
    beta = models.CharField(max_length=32)

class Author(models.Model):
    """
    """
    name = models.CharField(max_length=300)
    code = models.IntegerField()
    epsilon = models.CharField(max_length=33)

class Book(models.Model):
    """
    """
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    code = models.IntegerField(default=4)
    editor = models.ForeignKey(Editor)
    author = models.ForeignKey(Author)

