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

class Command(BaseCommand):
    help = 'Import datas'


    def handle(self, *args, **options):
        """
        Use keyset pagination
        """
        log = Log.objects.create(name='keypage',
                                 start=datetime.now(),
                                 stop=datetime.now())

        nb = 0
        keyid = 0

        while True:
            queryset = BigBook.objects.filter(serie=3)
            books = queryset.filter(keyid__gt=keyid).order_by('keyid')[:250]
            for book in books:
                keyid = book.keyid
                # do want you want here
                if book.nbpages > 500:
                    nb = nb + 1

            if len(books) < 250:
                break

        log.stop = datetime.now()
        log.save()
        print "keypage", log.stop - log.start, nb
