#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013,2014 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from optparse import make_option
from random import randrange
import time
import sys
from django.core.management.base import BaseCommand
from foo.tuna.models import Book, Editor, Author, Sinopsis


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-n",
                    "--nbvalues",
                    dest="nbvalues",
                    type="int",
                    help="number of values to input",
                    default=1),
        )

    def handle(self, *args, **options):
        """Lookup some objects
        """
        print "Book : {}".format(Book.objects.all().count())
        print "Editor : {}".format(Editor.objects.all().count())
        print "Author : {}".format(Author.objects.all().count())

        # remove 10% of tuples, be in first
        (count, delta) = self.list_delete(3)
        self.print_console('list_delete', count, delta)
        # remove other 10% of tuples
        (count, delta) = self.del_delete(2)
        self.print_console('del_delete', count, delta)
        # remove again 10% of tuples
        (count, delta) = self.regular_delete(1)
        self.print_console('regular_delete', count, delta)

        print "Book : {}".format(Book.objects.all().count())
        print "Editor : {}".format(Editor.objects.all().count())
        print "Author : {}".format(Author.objects.all().count())

    def print_console(self, name, count, delta):
        print "{:<15} {} time {} seconds".format(name, count, delta)
        
    def regular_delete(self, code):
        """Delete books with an evaluated QuerySet
        """
        start = time.time()

        books = Book.objects.filter(code=code)
        count = books.count()

        to_be_deleted_ref_list = [doc.id for doc in books]

        Book.objects.filter(pk__in=to_be_deleted_ref_list).delete()

        delta = time.time() - start
        return (count, delta)

    def del_delete(self, code):
        """Delete books directly
        """
        start = time.time()

        books = Book.objects.filter(code=code)
        count = books.count()

        Book.objects.filter(code=code).delete()

        delta = time.time() - start
        return (count, delta)

    def list_delete(self, code):
        """Delete books with a non evaluated QuerySet
        """
        ids = []

        start = time.time()

        books = Book.objects.filter(code=code)
        count = books.count()

        book_list = Book.objects.filter(code=code)
        Book.objects.filter(pk__in=book_list).delete()

        delta = time.time() - start

        return (count, delta)
