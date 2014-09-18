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
from foo.july.models import Book
import logging
from datetime import datetime

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
        Read the table book without TextField
        """
        self.offset()
        self.keypage()

    def offset(self):
        log = Log.objects.create(name='offset',
                                 start=datetime.now(),
                                 stop=datetime.now())

        nb = 0


        books = Book.objects.all().order_by('pk')
        paginator = Paginator(books, 250)
        for p in paginator.page_range:
            # loop on object_list
            for book in paginator.page(p).object_list:
                if book.nbpages > 500:
                    nb = nb + 1

        log.stop = datetime.now()
        log.save()
        print "offset", log.stop - log.start, nb


    def keypage(self):
        log = Log.objects.create(name='offset',
                                 start=datetime.now(),
                                 stop=datetime.now())

        nb = 0
        i = 0
        stop = False

        while stop == False:
            books = Book.objects.filter(id__gt=i).order_by('pk')[:250]
            for book in books:
                if book.nbpages > 500:
                    nb = nb + 1
                i = book.id
            if len(books) < 250:
                stop = True

        log.stop = datetime.now()
        log.save()
        print "keypage", log.stop - log.start, nb
