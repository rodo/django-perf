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
from django.core.management.base import BaseCommand
from foo.loader.models import Item
from optparse import make_option
from faker import Faker
from foo.loader.tasks import mul, insert
from foo.loader.models import Item


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-n",
                    "--nbvalues",
                    dest="nbvalues",
                    help="number of values to input",
                    default=10),
        )

    def handle(self, *args, **options):
        """
        Make
        """
        nbvalues = int(options['nbvalues'])
        print Item.objects.all().count()

        values = self.valueset(nbvalues, 1)
        start = time.time()
        for val in values:
            res = insert.delay([val])
        delta = time.time() - start
        print "insert {} in {} seconds linear".format(nbvalues, delta)

    def valueset(self, nbvalues, step):
        """
        Generate the values
        """
        values = []

        f = Faker()
        for i in range(nbvalues):
            values.append({"name": f.name(),
                           "datetms": float(f.latitude()),
                           "email": "{}-{}".format(step, f.email()),
                           "value": f.random_number() + step})

        return values
