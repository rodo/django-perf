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
from foo.log.models import Log


_ELMT_ = 250


psycopg2.extras.register_default_json(loads=lambda x: x)
#psycopg2.extras.register_default_json(loads=json.loads)


def now():
    return datetime.now()

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
        settings.DATABASES['default']['OPTIONS'] = {'application_name': 'hotel_lookup'}
        #sys.exit(1)
        
        r=50#10+randrange(40)
        step = 0
        a = self.lookup(r + step)
        b = self.lookup_id(r + 2 * step)
        c = self.lookup_related(r + 3 * step)
        d = self.lookup_relatedvalues(r + 4 * step)
        e = self.lookup_raw(r + 5 * step)
        f = self.lookup_rawmw(r + 6 * step)
        g = self.lookup_rawbest(r + 7 * step)
        h = self.lookup_related_all(r + 8 * step)        
        print "a %s\nb %s\nc %s\nd %s\ne %s\nf %s\ng %s\nh %s\n" % (a, b, c, d, e, f, g, h)
        
    def lookup(self, id):
        """Actual way
        """
        jtxt = []

        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_

        color_obj = HotelColor.objects.get(id=id)

        hotels = Hotel.objects.filter(color=color_obj).order_by('pk')[start:stop]

        while (len(hotels) > 0):
            for hotel in hotels:
                jtxt.append({'id': hotel.id,
                             'color': hotel.color.name,
                             'skin': hotel.skin.name})
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            hotels = Hotel.objects.filter(color=color_obj).order_by('pk')[start:stop]

        log.stop = now()
        log.info = 'legacy'
        log.key = len(jtxt)
        log.save()
        return json.dumps(jtxt)

    def lookup_id(self, id):
        """Actual way
        """
        jtxt = []
        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_

        hotels = Hotel.objects.filter(color_id=id).order_by('pk')[start:stop]

        while (len(hotels) > 0):
            for hotel in hotels:
                jtxt.append({'id': hotel.id,
                             'color': hotel.color.name,
                             'skin': hotel.skin.name})
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            hotels = Hotel.objects.filter(color_id=id).order_by('pk')[start:stop]

        res = json.dumps(jtxt)

        log.stop = now()
        log.info = 'id'
        log.key = len(jtxt)
        log.save()
        return res

    def lookup_related(self, id):
        """Actual way
        """
        jtxt = []

        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_

        hotels = Hotel.objects.select_related().filter(color_id=id).order_by('pk')[start:stop]

        while (len(hotels) > 0):
            for hotel in hotels:
                jtxt.append({'id': hotel.id,
                             'color': hotel.color.name,
                             'skin': hotel.skin.name})
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            hotels = Hotel.objects.select_related().filter(color_id=id).order_by('pk')[start:stop]

        res = json.dumps(jtxt)

        log.stop = now()
        log.info = 'related'
        log.key = len(jtxt)
        log.save()
        return res

    def lookup_related_all(self, id):
        """Actual way
        """
        jtxt = []

        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_

        hotels = Hotel.objects.select_related().filter(color_id=id).order_by('pk')[start:stop]

        while (len(hotels) > 0):
            for hotel in hotels:
                jtxt.append({'id': hotel.id,
                             'color': hotel.color.name,
                             'skin': hotel.skin.name})
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            hotels = Hotel.objects.select_related().filter(color_id=id).order_by('pk')[start:stop]

        res = json.dumps(jtxt)

        log.stop = now()
        log.info = 'related'
        log.key = len(jtxt)
        log.save()
        return res


    def lookup_relatedvalues(self, id):
        """Actual way
        """
        jtxt = []

        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_

        hotels = Hotel.objects.select_related().filter(color_id=id).extra(select={'skin': 'skin__name'}).values('id','color__name','skin__name').order_by('pk')[start:stop]

        while (len(hotels) > 0):
            for hotel in hotels:
                jtxt.append(hotels[0])
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            hotels = Hotel.objects.select_related().filter(color_id=id).extra(select={'skin': 'skin__name'}).values('id','color__name','skin__name').order_by('pk')[start:stop]

        res = json.dumps(jtxt)

        log.stop = now()
        log.info = 'relatedvalues'
        log.key = len(jtxt)
        log.save()
        return res


    def lookup_raw(self, id):
        """Raw query
        """
        jtxt = []

        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_

        sql = """
WITH rowa AS (
    SELECT h.id, hc.name color, hs.name skin
        from hotel_hotel h
        inner join hotel_hotelcolor hc on hc. id = h.color_id
        inner join hotel_hotelskin hs on hs.id = h.skin_id
        where hc.id=%s
        ORDER BY h.id LIMIT %s OFFSET %s
    )
SELECT array_to_json(array_agg(rowa.*)) FROM rowa
    """

        cursor = connection.cursor()

        cursor.execute(sql, [id, _ELMT_, start])
        rows = cursor.fetchone()

        while rows[0] is not None:
            j = json.loads(rows[0])
            jtxt = jtxt + j
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            cursor.execute(sql, [id, _ELMT_, start])
            rows = cursor.fetchone()

        res = json.dumps(jtxt)

        log.stop = now()
        log.info = 'raw'
        log.key = len(jtxt)
        log.save()
        return jtxt

    def lookup_rawmw(self, id):
        """Raw SQL without OFFSET
        """
        jtxt = []

        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_
        hid = 0

        sql = """
WITH rowa AS (
    SELECT h.id, hc.name color, hs.name skin
        from hotel_hotel h
        inner join hotel_hotelcolor hc on hc. id = h.color_id
        inner join hotel_hotelskin hs on hs.id = h.skin_id
        where hc.id=%s AND h.id > %s
        ORDER BY h.id LIMIT %s
    )
SELECT array_to_json(array_agg(rowa.*)) FROM rowa
    """

        cursor = connection.cursor()

        cursor.execute(sql, [id, hid, _ELMT_])
        rows = cursor.fetchone()

        while rows[0] is not None:
            j = json.loads(rows[0])
            jtxt = jtxt + j
            hid = j[-1][u'id']
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            cursor.execute(sql, [id, hid, _ELMT_])
            rows = cursor.fetchone()

        res = json.dumps(jtxt)

        log.stop = now()
        log.info = 'rawmw'
        log.key = len(jtxt)
        log.save()
        return jtxt

    def lookup_rawbest(self, id):
        """Raw SQL without OFFSET and direct access to last ID in query
        """
        jtxt = []

        log = Log.objects.create(name='hotel_lookup', start=now(), stop=now())

        loop = 0
        start = loop * _ELMT_
        stop = (loop + 1) * _ELMT_
        hid = 0

        sql = """
    WITH rowa AS (
    SELECT h.id, hc.name color, hs.name skin
        from hotel_hotel h
        inner join hotel_hotelcolor hc on hc. id = h.color_id
        inner join hotel_hotelskin hs on hs.id = h.skin_id
        where hc.id=%s AND h.id > %s
        ORDER BY h.id LIMIT %s
    )
SELECT CAST(array_to_json(array_agg(rowa.*)) AS TEXT),(select max(id) from rowa) FROM rowa
    """

        cursor = connection.cursor()

        cursor.execute(sql, [id, hid, _ELMT_])
        rows = cursor.fetchone()
        print rows[0]
        while rows[0] is not None:
            jtxt.append(rows[0])
            hid = rows[1]
            loop = loop + 1
            start = loop * _ELMT_
            stop = (loop + 1) * _ELMT_
            cursor.execute(sql, [id, hid, _ELMT_])
            rows = cursor.fetchone()

        res = "[%s]" % (",".join(jtxt))

        log.stop = now()
        log.info = 'rawbest'
        log.key = len(jtxt)
        log.save()
        return jtxt

