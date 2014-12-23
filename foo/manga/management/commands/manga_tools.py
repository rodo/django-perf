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
from foo.manga.models import Category, Genre


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
        """Lookup some objects
        """
        self.lookup_cat(3, 4)
        self.lookup_cat(5, 7)
        self.lookup_cat(20, 7)
        self.lookup_cat(13, 12)


    def lookup_cat(self, idx, comp):
        """Do lookups on categories
        """
        print "======================="
        parent = Category.objects.get(pk=idx)
        print parent.__unicode__()
        print "obj.root() : %s" % (unicode(parent.root()))
        print "obj.path() %s" % (parent.path.__str__())
        print "obj.depth() %s" % (parent.depth)
        print "obj.is_branch() %s" % (parent.is_branch())
        print "obj.is_leaf() %s" % (parent.is_leaf())
        print "obj.is_parent_of(%d) %s" % (comp,
                                             parent.is_parent_of(Category.objects.get(pk=comp)))
        print "obj.is_child_of(%d) %s" % (comp,
                                           parent.is_child_of(Category.objects.get(pk=comp)))
        print "obj.is_ancestor_of(%d) %s" % (comp,
                                             parent.is_ancestor_of(Category.objects.get(pk=comp)))
        print "obj.is_descendant_of(%d) %s" % (comp,
                                               parent.is_descendant_of(Category.objects.get(pk=comp)))
        print "obj.is_sibling_of(%d) %s" % (comp,
                                            parent.is_sibling_of(Category.objects.get(pk=comp)))


