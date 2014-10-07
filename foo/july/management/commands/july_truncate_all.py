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

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Import datas'

    def handle(self, *args, **options):
        """Empty all tables
        """
        cursor = connection.cursor()

        tables = ['july_bigbook',
                  'july_book',
                  'july_bookcomment',
                  'july_editor',
                  'july_translator',
                  'july_author']

        for table in tables:
            cursor.execute('TRUNCATE %s CASCADE' % table )
            cursor.execute("SELECT setval('%s_id_seq', 1)" % table)
