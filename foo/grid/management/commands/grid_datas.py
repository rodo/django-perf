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
from foo.grid.models import Grid, GridForeign
from faker import Faker


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

    def randarray(self):
        nbv = randrange(20)+1
        i = 0
        dat = []
        while i < nbv:
            i += 1
            dat.append(1+randrange(20000))
        return dat
            
    def handle(self, *args, **options):
        """Use autofixture to load datas
        """
        nbvalues = options['nbvalues']
        f = Faker()
        datasa = []
        datasi = []
        i = 1
        nba = 0
        for aux in range(nbvalues):
            tags = self.randarray()
            old = ",%s," % (",".join([str(b) for b in tags]))
            grid = Grid.objects.create(name=f.name(),
                                       alpha=f.word(),
                                       old=old,
                                       tags=tags)

            for tag in tags:
                GridForeign.objects.create(tag=tag,
                                           grid_id=grid.id)
