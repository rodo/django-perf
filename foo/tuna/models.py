from django.db import models

class Company(models.Model):
    """A Company with

    No relation to any other model
    """
    name = models.CharField(max_length=300)
    code = models.IntegerField()
    epsilon = models.CharField(max_length=33)


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
    code = models.IntegerField(default=4, db_index=True)
    author = models.ForeignKey(Author)
    deci = models.IntegerField(default=4, db_index=True)
    centi = models.IntegerField(default=40, db_index=True)
    milli = models.IntegerField(default=344, db_index=True)

class Editor(models.Model):
    """An editor
    """
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

# mis a jour par trigger
#
class Sinopsis(models.Model):
    """A company
    """
    text = models.TextField()
    book = models.ForeignKey(Book)
