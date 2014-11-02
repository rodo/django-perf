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
from datetime import datetime
from optparse import make_option
from random import randrange
from faker import Faker
from django.db import connection
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from django.db.models import F
from foo.apple.models import Apple
from foo.log.models import Log


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

        test = 'apple_update_F'

        log = Log.objects.create(name=test,
                                 start=datetime.now(),
                                 stop=datetime.now())

        indice = f.random_int(1,100)

        objs = Apple.objects.filter(indice=indice).update(keyid=F('indice'))

        log.stop = datetime.now()
        log.save()

        print test, log.stop - log.start
        print "indice %d -> %d items" % (indice, Apple.objects.filter(indice=indice).count())
