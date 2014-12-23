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
from faker import Faker
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
        make_option("-c",
                    "--childs",
                    dest="childs",
                    type="int",
                    help="number of childs to input",
                    default=randrange(10)),
        )

    def handle(self, *args, **options):
        """
        Make
        """
        f = Faker()
        nbvalues = options['nbvalues']

        childs = options  ['childs']
        catid = randrange(10)
        name = f.name()

        root = Category.objects.create(name=name,
                                       catid=catid)

        moot = Genre.objects.create(name=name,
                                    catid=catid)

        for aux in range(nbvalues):
            parent = root
            marent = moot
            for child in range(childs):
                catid = randrange(10)
                name = f.name()

                parent = Category.objects.create(name=name,
                                                 catid=catid,
                                                 parent=parent)

                marent = Genre.objects.create(name=name,
                                              catid=catid,
                                              parent=marent)

        print Category.objects.all().count()
        print Genre.objects.all().count()
