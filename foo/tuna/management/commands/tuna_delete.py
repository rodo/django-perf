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
from foo.tuna.models import Book, Editor, Author, Company, Sinopsis


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-c",
                    "--code",
                    dest="code",
                    type="int",
                    help="number of values to input",
                    default=1),
        )

    def handle(self, *args, **options):
        """Lookup some objects
        """
        code = options['code']
        self.doit(code, Book, 'Book')
        self.doit(code, Company, 'Company')

    def doit(self, code, model, name):

        print "{} : {}".format(name, model.objects.all().count())

        # remove 10% of tuples, be in first
        (count, delta) = self.raw_delete(code + 3, model)
        self.print_console('raw_delete', count, delta)
        # remove 10% of tuples, be in first
        (count, delta) = self.list_delete(code + 2, model)
        self.print_console('list_delete', count, delta)
        # remove other 10% of tuples
        (count, delta) = self.del_delete(code + 1, model)
        self.print_console('del_delete', count, delta)
        # remove again 10% of tuples
        (count, delta) = self.regular_delete(code, model)
        self.print_console('regular_delete', count, delta)

        print "{} : {}".format(name, model.objects.all().count())


    def print_console(self, name, count, delta):
        print "{:<15} {} time {} seconds".format(name, count, delta)
        
    def regular_delete(self, code, model):
        """Delete books with an evaluated QuerySet
        """
        start = time.time()

        books = model.objects.filter(code=code)
        count = books.count()

        to_be_deleted_ref_list = [doc.id for doc in books]

        model.objects.filter(pk__in=to_be_deleted_ref_list).delete()

        delta = time.time() - start
        return (count, delta)

    def del_delete(self, code, model):
        """Delete books directly
        """
        start = time.time()

        books = model.objects.filter(code=code)
        count = books.count()

        model.objects.filter(code=code).delete()

        delta = time.time() - start
        return (count, delta)

    def list_delete(self, code, model):
        """Delete books with a non evaluated QuerySet
        """

        model.objects.raw("SELECT 'list_delete'") 
        start = time.time()

        books = model.objects.filter(code=code)
        count = books.count()

        book_list = model.objects.filter(code=code)

        model.objects.filter(pk__in=book_list).delete()

        delta = time.time() - start

        return (count, delta)

    def raw_delete(self, code, model):
        """Delete books with raw  commands
        """
        start = time.time()

        books = model.objects.filter(code=code)
        count = books.count()

        model.objects.raw("DELETE FROM tuna_editor_books WHERE book_id IN (SELECT id FROM tuna_book WHERE code=%s", [code])
        model.objects.raw("DELETE FROM tuna_sinopsis WHERE book_id IN (SELECT id FROM tuna_book WHERE code=%s", [code])
        model.objects.raw("DELETE FROM tuna_book WHERE code=%s", [code])
        delta = time.time() - start

        return (count, delta)
