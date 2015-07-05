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
import json
from django.conf import settings
from optparse import make_option
from random import randrange
from faker import Faker
from django.db import connection
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from foo.hotel.models import Hotel
from foo.hotel.models import HotelColor
from foo.hotel.models import HotelSkin
from foo.hotel.models import HotelDoor
from foo.hotel.models import HotelCompany


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
        hotel
        """
        settings.DATABASES['default']['OPTIONS'] = {'application_name': 'hotel_datas'}
        nbvalues = options['nbvalues']
        colors = self.colors(HotelColor, nbvalues)
        skins = self.colors(HotelSkin, nbvalues)
        doors = self.colors(HotelDoor, nbvalues)
        companies = self.colors(HotelCompany, nbvalues)
        self.hotels(nbvalues, colors, skins, doors, companies)
        
    def colors(self, instance, nbvalues):
        f = Faker()
        nba = 0
        datas = []
        for aux in range(max(1, nbvalues / 10)):
            datas.append(instance(name=f.last_name()[:30],
                                  indice=randrange(100),
                                  foo=randrange(100),
                                  bar=randrange(100),
                                  alpha=" ".join(f.words(30))))

            nba += 1
            if nba > 9:
                instance.objects.bulk_create(datas)
                datas = []
                nba = 0

        cc = instance.objects.all().count()
        print "%s objects %s db" % (cc,
                                    instance.__name__)
        return cc

    def hotels(self, nbvalues, colors, skins, doors, companies):
        f = Faker()
        nba = 0
        datas = []
        for aux in range(nbvalues):

            datas.append(Hotel(name=f.last_name()[:30],
                               indice=randrange(1000),
                               color_id=max(1,randrange(colors) - 1),
                               skin_id=max(1, randrange(skins) - 1),
                               door_id=max(1, randrange(doors) - 1),
                               company_id=max(1, randrange(companies) - 1),
                               objtxt=" ".join(f.words(30))))
            nba += 1
            if nba > 9:
                Hotel.objects.bulk_create(datas)
                datas = []
                nba = 0

        print "%s objects in db" % (Hotel.objects.all().count())
