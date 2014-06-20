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
from django.db import connection


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
        print Item.objects.all().count()
        for bulk in [1, 2, 10]:
            values = self.valueset(nbvalues, bulk)
            start = time.time()
            self.bulkinsert(values, bulk)
            delta = time.time() - start
            print "insert {} in {} seconds bulk {}".format(nbvalues,
                                                           delta,
                                                           bulk)

        values = self.valueset(nbvalues, bulk)
        start = time.time()
        self.insert(values)
        delta = time.time() - start
        print "insert {} in {} seconds linear".format(nbvalues, delta)

        values = self.valueset(nbvalues, bulk)
        start = time.time()
        self.insertcopy(values)
        delta = time.time() - start
        print "copy   {} in {} seconds".format(nbvalues, delta)
        print Item.objects.all().count()

    def valueset(self, nbvalues, step):
        """
        Generate the values
        """
        values = []

        f = Faker()
        for i in range(nbvalues):
            values.append({"name": f.name(),
                           "datetms": f.latitude(),
                           "email": "{}-{}".format(step, f.email()),
                           "value": f.random_number() + step})

        return values

    def insert(self, values):
        """
        Save values in DB
        """
        for val in values:
            Item.objects.create(datetms=val['datetms'],
                                name=val['name'],
                                email=val['email'],
                                value=val['value'])

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

            for val in values[low:high]:
                poms.append(Item(datetms=val['datetms'],
                                name=val['name'],
                                email=val['email'],
                                value=val['value']))

            Item.objects.bulk_create(poms)
            i = i + 1

        if high < nbval:
            for val in values[high:nbval]:
                poms.append(Item(datetms=val['datetms'],
                                name=val['name'],
                                email=val['email'],
                                value=val['value']))

            Item.objects.bulk_create(poms)

    def insertcopy(self, values):
        """
        Use COPY to insert datas
        """
        fields = ['datetms', 'name', 'email', 'value']
        strfields = ",".join(fields)
        raw = 'COPY loader_item ({}) FROM \'{}\' USING DELIMITERS \',\';'

        fpath = '/tmp/foo'
        f = open(fpath, 'w')
        for val in values:
            f.write('{},"{}","{}",{}\n'.format(val['datetms'],
                                           val['name'],
                                           val['email'],
                                           val['value']))
        f.close()
        cursor = connection.cursor()
        cursor.copy_from(open(fpath, 'r'), 'loader_item', columns=tuple(fields), sep=',')

