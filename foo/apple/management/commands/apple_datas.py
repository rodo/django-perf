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
from faker import Faker
from django.db import connection
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from foo.apple.models import Apple


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

        nba = 0
        datas = []
        for aux in range(nbvalues):
            datas.append(Apple(name=f.last_name()[:30],
                               indice=f.random_int(1,100),
                               keyid=f.random_int(1,100),
                               bigrand=f.random_int(1,10000),
                               idx_bigrand=f.random_int(1,10000),
                               idx_tinyrand=f.random_int(1,10),
                               tinyrand=f.random_int(1,10),
                               alpha = f.word(),
                               beta = f.word(),
                               gamma = f.word(),
                               delta  = f.word(),
                               epsilon  = f.word(),
                               zeta = f.word(),
                               intro = f.words(),
                               synopsis = f.words(500)))


            nba += 1
            if nba > 9:
                Apple.objects.bulk_create(datas)
                datas = []
                nba = 0

        print Apple.objects.all().count()
