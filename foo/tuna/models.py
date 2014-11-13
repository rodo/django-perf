from django.db import models


class Editor(models.Model):
    """An editor
    """
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=150)


class Company(models.Model):
    """A company
    """
    family = models.CharField(max_length=300)
    beta = models.CharField(max_length=32)


class Author(models.Model):
    """An author
    """
    name = models.CharField(max_length=300)
    code = models.IntegerField()
    epsilon = models.CharField(max_length=33)


class Book(models.Model):
    """A book
    """
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    code = models.IntegerField(default=4)
    editor = models.ForeignKey(Editor)
    author = models.ForeignKey(Author)
