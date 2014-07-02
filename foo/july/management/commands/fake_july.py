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
from foo.july.models import Company, Orga, Entry
from django.contrib.sites.models import Site


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
        f = Faker()
        nbvalues = options['nbvalues']
        print "Company : {}".format(Company.objects.all().count())

        for i in range(nbvalues):
            comp = Company.objects.create(site_id=2,
                                          name=f.last_name()[:30])

            for o in range(4):
                Orga.objects.bulk_create([Orga(site_id=comp.site_id,
                                               company=comp,
                                               name=f.last_name()[:30])])

                orga = Orga.objects.all().last()

                for e in range(100):
                    entry = Entry.objects.create(site_id=comp.site_id,
                                                 name=f.last_name()[:30])
                    entry.companies.add(comp)
                    entry.orgas.add(orga)

                
        print "Company : {}".format(Company.objects.all().count())
