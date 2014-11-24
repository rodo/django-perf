#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of django-json-dbindex nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
from django.core.management.base import BaseCommand
from optparse import make_option
from ... import util


class Command(BaseCommand):
    help = 'Import datas'
    option_list = BaseCommand.option_list + (
        make_option("-s",
                    "--simulate",
                    dest="simulate",
                    action="store_true",
                    help="number of values to input",
                    default=False),
        make_option("-t",
                    "--table",
                    dest="table",
                    type="string",
                    help="table name",
                    default=None),
        make_option("-c",
                    "--column",
                    dest="column",
                    type="string",
                    help="column name",
                    default=None),
        )


    def handle(self, *args, **options):
        """
        Handle action
        """
        for trig in util.get_app_paths():
            self.create_trigger(trig, options['simulate'])
        

    def create_trigger(self, trig, simulate):
        """
        {'table': u'apple_apple',
         'model': <class 'foo.apple.models.Apple'>,
         'aggs': ['max'],
         'field': 'indice'}        
        """
        aggs = ['count']
        column = trig['field']
        table = trig['table']

        agg = util.AggTrigger()

        if table and column and len(aggs) > 0:
        
            if not simulate:
                print agg.create_objects(table, column, aggs)
            else:
                for sql in agg.sql_create_functions(table, column, aggs):
                    print sql
                for sql in agg.sql_create_triggers(table, column):
                    print sql
                print agg.sql_create_table(table, column, aggs)
