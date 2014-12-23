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
from foo.manga.models import Category, Genre


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-n",
                    "--nbvalues",
                    dest="nbvalues",
                    type="int",
                    help="number of values to input",
                    default=10),
        )

    def handle(self, *args, **options):
        """Lookup some objects
        """
        ids = []
        nbv = 100
        for aux in range(nbv):
            ids.append(randrange(100)+100)

        self.lookup_cat(ids, nbv)
        self.lookup_genre(ids, nbv)

    def lookup_cat(self, ids, nbv):
        """Do lookups on categories
        """
        lastid = 13
        count = 0
        start = time.time()

        for idx in ids:
            try:
                parent = Category.objects.get(pk=idx)
                old = Category.objects.get(pk=lastid)
                qry = Category.objects.get(pk=parent.parent_id).is_child_of(old)
                lastid = parent.id
                if qry:
                    count += 1

            except:
                print idx

        delta = time.time() - start
        print "{} categories in {} seconds, {}".format(nbv, delta, count)


    def lookup_genre(self, ids, nbv):
        """Do lookups on Genre
        """
        count = 0
        lastid = 13
        start = time.time()

        for idx in ids:
            try:
                parent = Genre.objects.get(pk=idx)
            except:
                print idx
                sys.exit(1)
            old = Genre.objects.get(pk=lastid)
            qry = Genre.objects.get(pk=parent.parent_id).is_descendant_of(old)
            lastid = parent.id
            if qry:
                count += 1

        delta = time.time() - start
        print "{} genres in {} seconds {}".format(nbv, delta, count)
