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
from foo.tuna.models import Book, Editor, Author


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

        self.regular_delete(1)
        self.del_delete(2)
        self.list_delete(3)

        print "Book : {}".format(Book.objects.all().count())
        print "Editor : {}".format(Editor.objects.all().count())
        print "Author : {}".format(Author.objects.all().count())

    def regular_delete(self, code):
        """Delete books with an evaluated QuerySet
        """
        start = time.time()

        books = Book.objects.filter(code=code)
        count = books.count()

        to_be_deleted_ref_list = [doc.id for doc in books]

        Book.objects.filter(pk__in=to_be_deleted_ref_list).delete()

        delta = time.time() - start
        print "regular_delete {} time {} seconds".format(count, delta)

    def del_delete(self, code):
        """Delete books directly
        """
        start = time.time()

        books = Book.objects.filter(code=code)
        count = books.count()

        Book.objects.filter(code=code).delete()

        delta = time.time() - start
        print "del_delete {} time {} seconds".format(count, delta)

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
        print "{} time {} {} seconds".format('list_delete', count, delta)
