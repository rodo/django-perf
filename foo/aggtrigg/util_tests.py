#! /usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Rodolphe Quiedeville <rodolphe@quiedeville.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, sys
import syslog
import unittest
import util
#from mock import Mock, patch


class utilTests(unittest.TestCase):

    def setUp(self):
        self.agg = util.AggTrigger()        

    def test_init(self):
        self.assertEqual('default', self.agg.database)

    def test_function_name(self):
        self.assertEqual("foo_colfoo_insert()",
                         util.function_name('foo', 'colfoo', 'insert'))

    def test_trigger_name(self):
        self.assertEqual("foo_insert_trigger",
                         util.trigger_name('foo', 'insert'))

    def test_sql_create_trigger(self):
        res = self.agg.sql_create_trigger('foo', 'insert', 'function_called()')        
        self.assertEqual("CREATE", res[:6])

    def test_sql_create_triggers(self):
        res = self.agg.sql_create_triggers('table', 'column')
        self.assertEqual(len(res), 3)
        self.assertTrue(isinstance(res, list))

    def test_sql_create_function(self):
        agg = util.AggTrigger()        
        res = agg.sql_create_function('book', 'nbpage', ['count'], 'insert')
        self.assertTrue(isinstance(res, unicode))
        self.assertTrue(len(res) > 10)

    def test_sql_create_functions(self):
        agg = util.AggTrigger()        
        res = agg.sql_create_functions('book', 'nbpage', ['count'])
        self.assertTrue(isinstance(res, list))
        self.assertEqual(len(res), 3)

    def test_sql_drop_functions(self):
        agg = util.AggTrigger()        
        res = agg.sql_drop_functions('book', 'bar')
        self.assertTrue(isinstance(res, list))
        self.assertEqual(len(res), 3)

    def test_sql_drop_triggers(self):
        agg = util.AggTrigger()        
        res = agg.sql_drop_triggers('book')
        self.assertTrue(isinstance(res, list))
        self.assertEqual(len(res), 3)

    def test_sql_create_table(self):
        """Test with only one aggregat
        """
        res = self.agg.sql_create_table('book', 'nbpage', ['count'])
        self.assertTrue(isinstance(res, unicode))
        self.assertTrue(len(res) > 3)

    def test_sql_create_table_twoagg(self):
        """Test with two aggregats
        """
        res = self.agg.sql_create_table('book', 'nbpage', ['count','min'])
        self.assertTrue(isinstance(res, unicode))
        self.assertTrue(len(res) > 3)

    def test_sql_drop_trigger(self):
        res = self.agg.sql_drop_trigger('foo', 'table_bar')
        self.assertTrue(isinstance(res, str))
        # TODO mov test to pgTests
        #self.assertEqual(res, 'DROP TRIGGER IF EXISTS foo ON table_bar')

    def test_sql_drop_function(self):
        res = self.agg.sql_drop_function('foo')
        self.assertTrue(isinstance(res, str))

    def test_sql_drop_table(self):
        res = self.agg.sql_drop_table('table_bar')
        self.assertTrue(isinstance(res, str))

