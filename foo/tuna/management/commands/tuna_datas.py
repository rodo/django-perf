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

import sys
import os
import time
from optparse import make_option
from random import randrange
from autofixture import AutoFixture
from django.db import connection
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from foo.tuna.models import Book, Author, Editor, Company
from faker import Faker


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-n",
                    "--nbvalues",
                    dest="nbvalues",
                    type="int",
                    help="number of values to input",
                    default=100),
        )

    def handle(self, *args, **options):
        """Use autofixture to load datas
        """
        nb = options['nbvalues']

        f = Faker()
        nbvalues = options['nbvalues']

        nba = 0
        datas = []
        comps = []
        name = f.name()

        author = Author.objects.create(name=name,
                                       code=randrange(10),
                                       epsilon=f.word())

        editor = Editor.objects.create(name=name,
                                       country=f.country())

        i = 1
        for aux in range(nbvalues):
            i += 1
            name = f.name()

            if str(i).endswith('5'):
                author = Author.objects.create(name=name,
                                               code=randrange(10),
                                               epsilon=f.word())

            if str(i).endswith('0'):
                author = Author.objects.create(name=name,
                                               code=f.pyint(),
                                               epsilon=f.word())

                editor = Editor.objects.create(name=name,
                                               country=f.country())

            datas.append(Book(author=author,
                              deci=randrange(10),
                              centi=randrange(100),
                              milli=randrange(1000),
                              title=" ".join(f.words())[:30],
                              code=randrange(6)))

            comps.append(Company(name=name,
                                 code=randrange(6),
                                 epsilon=f.word()))

            nba += 1
            if nba > 9:
                Company.objects.bulk_create(comps)
                Book.objects.bulk_create(datas)
                datas = []
                comps = []
                nba = 0

        print "Book : {}".format(Book.objects.all().count())
        print "Company : {}".format(Company.objects.all().count())
        print "Editor : {}".format(Editor.objects.all().count())
        print "Author : {}".format(Author.objects.all().count())
