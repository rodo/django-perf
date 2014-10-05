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
import imp
from django.core.management.base import BaseCommand
from optparse import make_option
from django.core.paginator import Paginator
from foo.offset.models import Log
from foo.july.models import BigBook
import logging
from datetime import datetime
from django.db import connection

class Command(BaseCommand):
    help = 'Import datas'


    def handle(self, *args, **options):
        """
        Use prepared query on july_bigbook

        """
        key = 'keypage_prepare_fields'
        log = Log.objects.create(name=key,
                                 start=datetime.now(),
                                 stop=datetime.now())

        nb = 0
        keyid = 0

        cursor = connection.cursor()

        try:
            cursor.execute('DEALLOCATE preptwo')
        except:
            pass

        qry = " ".join(["PREPARE preptwo (integer) AS ",
                        "SELECT keyid,nbpages FROM july_bigbook",
                        "WHERE serie= 3 AND keyid > $1",
                        "ORDER BY keyid ASC LIMIT 250"])

        try:
            cursor.execute(qry)
        except:
            pass

        while True:
            cursor.execute('EXECUTE preptwo (%s)' % (keyid))
            books = cursor.fetchall()
            for book in books:
                keyid = book[0]
                # do want you want here
                if book[1] > 500:
                    nb = nb + 1

            if len(books) < 250:
                break

        log.stop = datetime.now()
        log.save()
        print key, log.stop - log.start, nb
