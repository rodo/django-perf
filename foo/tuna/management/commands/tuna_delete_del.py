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
from optparse import make_option
from random import randrange
import time
import sys
from django.core.management.base import BaseCommand
from foo.tuna.models import Book, Editor, Author, Company, Sinopsis
import utils


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-c",
                    "--code",
                    dest="code",
                    type="int",
                    help="number of values to input",
                    default=1),
        )

    def handle(self, *args, **options):
        """Lookup some objects
        """
        code = options['code']
        self.doit(code, Book, 'Book')
        self.doit(code, Company, 'Company')

    def doit(self, code, model, name):

        print "{} : {}".format(name, model.objects.all().count())

        # remove 10% of tuples, be in first
        (count, delta) = utils.del_delete(code + 3, model)
        utils.print_console('del_delete', count, delta)

        print "{} : {}".format(name, model.objects.all().count())


