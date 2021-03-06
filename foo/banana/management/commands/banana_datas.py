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
from foo.banana.models import Fruit, Color, Banana, Owner, Variety


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
        """Use autofixture to load datas
        """
        nb = options['nbvalues']

        fixowner = AutoFixture(Owner)
        entries = fixowner.create(20 * nb)

        fixvariety = AutoFixture(Variety)
        entries = fixvariety.create(5 * nb)

        fixcolor = AutoFixture(Color)
        entries = fixcolor.create(4 * nb)

        fixfruit = AutoFixture(Fruit)
        entries = fixfruit.create(nb)

        fixbanana = AutoFixture(Banana)
        entries = fixbanana.create(10 * nb)

        print Fruit.objects.all().count()
        print Color.objects.all().count()
        print Banana.objects.all().count()
