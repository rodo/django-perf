from django.db import models
from django.contrib.sites.models import Site


class Editor(models.Model):
    """
    A big table
    """
    name = models.CharField(max_length=30)


    class Admin:
        pass


class Author(models.Model):
    """
    The author
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Translator(models.Model):
    """
    A big table
    """
    name = models.CharField(max_length=30)


class Book(models.Model):
    """
    The books
    """
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=30)
    serie = models.IntegerField(default=0)
    nbpages = models.IntegerField(default=0)
    editors = models.ManyToManyField(Editor, blank=True)
    translators = models.ManyToManyField(Translator, blank=True)


class BookComment(models.Model):
    book = models.ForeignKey(Book)
    synopsis = models.TextField(blank=True)


class BigBook(models.Model):
    """
    The books
    """
    keyid = models.IntegerField(unique=True)
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=30)
    serie = models.IntegerField(default=0)
    nbpages = models.IntegerField(default=0)
    editors = models.ManyToManyField(Editor, blank=True)
    translators = models.ManyToManyField(Translator, blank=True)
    synopsis = models.TextField(blank=True)
    intro = models.TextField(blank=True)
