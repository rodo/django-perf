#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Rodolphe Quiédeville <rodolphe@quiedeville.org>
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
from foo.loader.models import ComplexItem, Company
from optparse import make_option
from faker import Faker
from django.db import connection


class Command(BaseCommand):
    help = 'Import complex datas'
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
        Main
        """
        nbvalues = options['nbvalues']
        bulk = 2
        self.companies()

        print ComplexItem.objects.all().count()

        for bulk in [1, 2, 10, 50]:
            values = self.valueset(nbvalues, bulk)
            start = time.time()
            self.bulkinsert(values, bulk)
            delta = time.time() - start
            print "insert {} in {} seconds bulk {}".format(nbvalues, delta, bulk)

        values = self.valueset(nbvalues, bulk)
        start = time.time()
        self.insert(values)
        delta = time.time() - start
        print "insert {} in {} seconds linear".format(nbvalues, delta)

        values = self.valueset(nbvalues, 4)
        start = time.time()
        self.insertcopy(values)
        delta = time.time() - start
        print "copy   {} in {} seconds".format(nbvalues, delta)

        print ComplexItem.objects.all().count()

    def valueset(self, nbvalues, step):
        """
        Generate the values
        """
        values = []
        
        f = Faker()
        for i in range(nbvalues):
            values.append({"company": 3,
                           "name": f.name()[:300], 
                           "street_address": f.street_address()[:300],
                           "email": "{}-{}".format(step,f.email()),
                           "value": f.random_number() + step,
                           "vali": f.random_number() + step,
                           "country": f.country()[:100], 
                           "latitude": f.latitude(),                            
                           "longitude": f.longitude(),
                           "city": f.city()[:50],
                           "city_suffix": f.city_suffix()[:20],
                           "locale": f.locale()[:8],
                           })

        return values

    def insert(self, values):
        """
        Linear inserts
        """
        for val in values:
            """

            """
            ComplexItem.objects.create(company=Company(pk=val['company']),
                                       name=val['name'],
                                       street_address=val['street_address'],
                                       email=val['email'],
                                       value=val['value'],
                                       vali=val['vali'],
                                       country=val['country'],
                                       latitude=val['latitude'],
                                       longitude=val['longitude'],
                                       city=val['city'],
                                       city_suffix=val['city_suffix'],
                                       locale=val['locale'])

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
            self.dobulk(values, low, high)
            i = i + 1 

        if high < nbval:
            self.dobulk(values, high, nbval)


    def dobulk(self, values, low, high):
        """
        Do bulk insert on DB

        values (array)
        low (integer)
        high(integer)
        """
        poms = []
        for val in values[low:high]:
            poms.append(ComplexItem(company=Company(pk=val['company']),
                                    name=val['name'],
                                    street_address=val['street_address'],
                                    email=val['email'],
                                    value=val['value'],
                                    vali=val['vali'],
                                    country=val['country'],
                                    latitude=val['latitude'],
                                    longitude=val['longitude'],
                                    city=val['city'],
                                    city_suffix=val['city_suffix'],
                                    locale=val['locale']))

        ComplexItem.objects.bulk_create(poms)


    def insertcopy(self, values):
        """
        Save values in DB
        """
        pattern = '%s%s{}\n' % ('"{}",' * 7, '{},' * 4)
        fpath = '/tmp/foo'
        f = open(fpath,'w')
        for val in values:
            """

            """
            f.write(pattern.format(val['name'],
                                   val['street_address'],
                                   val['email'],
                                   val['country'],
                                   val['city'],
                                   val['city_suffix'],
                                   val['locale'],
                                   val['latitude'],
                                   val['longitude'],
                                   val['value'],
                                   val['vali'],
                                   val['company']
                                   ))
            

        f.close()
        fields = ['name', 'street_address', 'email', 'country', 
                  'city', 'city_suffix', 'locale', 'latitude', 
                  'longitude', 'value', 'vali', 'company_id']
        cursor = connection.cursor()        
        cursor.copy_from(open(fpath, 'r'), 'loader_complexitem', columns=tuple(fields), sep=',')

    def companies(self):
        """
        Save values in DB
        """
        f = Faker()
        for i in range(100):
            Company.objects.create(name= f.name(),
                                   country = f.country())
