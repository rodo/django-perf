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
from foo.loader.utils import valueset
from foo.loader.tasks import copyinsert
from foo.loader.models import Item


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-n",
                    "--nbvalues",
                    dest="nbvalues",
                    type="int",
                    help="number of values to input",
                    default=10),
        make_option("-b",
                    "--bulk",
                    dest="bulk",
                    type="int",
                    help="number of values to input",
                    default=10),)

    def handle(self, *args, **options):
        """
        Main
        """
        bulk = options['bulk']
        nbvalues = max(20, int(options['nbvalues']))
        method = "copy{}".format(bulk)
        Item.objects.filter(method=method).delete()
        print Item.objects.all().count()
        #
        # bulk
        # 

        values = valueset(nbvalues, bulk)
        start = time.time()
        self.launchbulk(values, bulk)
        delta = time.time() - start
        print "insert {} in {} seconds bulk {}".format(nbvalues, delta, bulk)

    def launchbulk(self, values, nb):
        """
        values (array)
        nb (interger) : number of task launched
        """
        i = 0
        high = 0
        nbval = len(values)
        method = "copy{}".format(nb)

        while high < nbval:
            poms = []
            low = i * nb
            high = low + nb
            copyinsert.delay(values[low:high], method)
            i = i + 1 

        print "launched {} bulk of {} element each  {}".format(i, nb, i * nb)
