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
from optparse import make_option
from faker import Faker
from django.db import connection
from foo.indexes.models import BigItem
from foo.indexes.utils import dobulk

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
        """
        Make
        """
        nbvalues = options['nbvalues']
        print BigItem.objects.all().count()
        for bulk in [1, 2, 10]:
            values = self.valueset(nbvalues, bulk)
            start = time.time()
            self.bulkinsert(values, bulk)
            delta = time.time() - start
            print "insert {} in {} seconds bulk {}".format(nbvalues,
                                                           delta,
                                                           bulk)


    def valueset(self, nbvalues, step):
        """
        Generate the values
        """
        values = []

        f = Faker()
        for i in range(nbvalues):
            
            country = f.country()[:100]
            color = f.color_name()[:20]

            values.append({"first_name": f.first_name()[:30],
                           "last_name": f.last_name()[:30],
                           "latitude": f.latitude(),
                           "longitude": f.longitude(),
                           "email": f.email(),
                           "email2": f.email(),
                           "address": f.street_address()[:300],
                           "address2": f.street_address()[:300],
                           "address3": f.street_address()[:300],
                           "city_suffix": f.city_suffix()[:20],
                           "city": f.city()[:50],
                           "code1": f.pyint(),
                           "code2": f.pyint(),
                           "code3": f.pyint(),
                           "code4": abs(f.pyint()),
                           "country1": country,
                           "country2": country,
                           "color1": color,
                           "color2": color,
                           "description1": f.sentence(100),
                           "description2": f.sentence(300),
                           "description3": f.sentence(50),
                           "price1": f.pyfloat(),
                           "price2": f.pyfloat(),
                           "price3": f.pyfloat()
                           })


        return values

    def bulkinsert(self, values, nb):
        """
        Save values in DB
        """
        i = 0
        nbval = len(values)
        part = int(round(nbval / nb))

        while i < nb:
            poms = []
            low = i * part
            high = low + part
            dobulk(values, "bulk", low, high)
            i = i + 1

        if high < nbval:
            dobulk(values, "bulk", high, nbval)
