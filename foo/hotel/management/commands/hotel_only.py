#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013,2015 Rodolphe Quiédeville <rodolphe@quiedeville.org>
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
from django.conf import settings
from django.db import connection
from django import db
import psycopg2
import psycopg2.extras
import sys
import os
import time
from datetime import datetime
import json
from optparse import make_option
from random import randrange

from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from foo.hotel.models import Hotel
from foo.hotel.models import HotelColor


class Command(BaseCommand):

    def handle(self, *args, **options):
        settings.DATABASES['default']['OPTIONS'] = {'application_name': 'hotel_only'}

        hotels = Hotel.objects.filter(color__indice=3).order_by('pk')[:5]

        hotels.query.clear_select_clause()
        hotels.query.add_fields(['name','color__name','indice'])

        print hotels

        for hotel in hotels:
            print hotel.name


        #
        hotels = Hotel.objects.filter(indice=3).order_by('pk')[:5]

        hotels.query.clear_select_clause()
        hotels.query.add_fields(['name','objtxt'])

        for hotel in hotels:
            print hotel.name
        
