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
from django.db.models import get_models
from django.conf import settings
import pgcommands
import databases


FILENAME_CREATE = 'dbindex_create.json'
FILENAME_DROP = 'dbindex_drop.json'


class DatabaseNotSupported(Exception):
    pass


class DatabaseUnknown(Exception):
    pass


class ActionUnknown(Exception):
    pass


def function_name(table, column, action):
    return "{0}_{1}_{2}()".format(table, column, action)


def trigger_name(table, action):
    return "{0}_{1}_trigger".format(table, action)


def table_name(table, column):
    """Compute the table name

    table (string) : the originate table's name
    column : the column name

    return : string
    """
    return "{0}_{1}_agg".format(table, column)


class AggTrigger(object):

    ACTIONS = ['insert', 'update', 'delete']
    ACTIONS = ['insert', 'update', 'delete']
    database = 'default'

    def __init__(self, database='default'):

        self.database = database

        # use the right backend
        if database in settings.DATABASES:
            if settings.DATABASES[database]['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
                from databases.pg import TriggerPostgreSQL
                self.backend = TriggerPostgreSQL()
            else:
                raise DatabaseNotSupported()
        else:
            raise DatabaseUnknown()

    def create_objects(self, table, column, aggregats):
        """Create all needed objects
        table (string)
        column (string)
        aggregats (array)
        """

        res = self.create_table(table_name(table, column),
                                column,
                                aggregats)

        res = self.create_functions(table, column, aggregats)
        res = self.create_triggers(table, column)

        return res

    def drop_objects(self, table, column):
        """Drop all relations from database
        table (string)
        column (string)
        """
        res = self.drop_triggers(table)

        res = self.drop_functions(table, column)

        res = self.drop_table(table_name(table, column))

        return res

    def create_table(self, name, column, aggregats):
        """
        table (string)
        column (string)
        aggregats (array)
        """
        sql = self.sql_create_table(name, column, aggregats)
        return pgcommands.execute_raw(sql, self.database)

    def create_triggers(self, table, column):
        res = 0
        for sql in self.sql_create_triggers(table, column):
            if res == 0:
                res = pgcommands.execute_raw(sql, self.database)
        return res

    def create_functions(self, table, column, aggregats):
        res = 0
        for sql in self.sql_create_functions(table, column, aggregats):
            if res == 0:
                res = pgcommands.execute_raw(sql, self.database)
        return res

    def sql_create_table(self, name, column, aggreggats):
        """
        table (string)
        column (string)
        aggregats (array)
        """
        return self.backend.sql_create_table(name, column, aggreggats)

    def sql_init(name):
        """
        Remplissage de la table technique avec les données existantes
        """

        sql = """
        """
        return sql

    def sql_create_triggers(self, table, column):
        """Declaration des triggers
        """
        sql = []
        for action in self.ACTIONS:
            function = function_name(table, column, action)
            sql.append(self.sql_create_trigger(table, action, function))

        return sql

    def sql_create_trigger(self, table, action, function):
        """
        table (string): table name
        action (string): insert, update or create
        function (string): function's name called by the trigger
        """
        return self.backend.sql_create_trigger(trigger_name(table, action),
                                               function,
                                               table,
                                               action)

    def drop_table(self, name):
        sql = self.sql_drop_table(name)
        return pgcommands.execute_raw(sql)

    def drop_functions(self, name, column):

        for sql in self.sql_drop_functions(name, column):
            pgcommands.execute_raw(sql)

    def sql_drop_functions(self, table, column):
        """
        Functions appellées par les triggers
        """
        sql = []
        for action in self.ACTIONS:
            sql.append(self.sql_drop_function(function_name(table,
                                                            column,
                                                            action)))

        return sql

    def sql_create_functions(self, table, column, aggregats):
        """Create all functions

        table (string)
        column (string)
        aggregats (array)
        """
        sql = []
        for action in self.ACTIONS:
            sql.append(self.sql_create_function(table,
                                                column,
                                                aggregats,
                                                action))
        return sql

    def sql_create_function(self, table, column, aggregats, action):
        """
        table (string)
        column (string)
        aggregats (array)
        action (string)
        """
        fname = function_name(table, column, action)
        tname = table_name(table, column)
        sql = None
        if action == 'insert':
            sql = self.backend.sql_create_function_insert(fname,
                                                          table,
                                                          column,
                                                          tname)

        elif action == 'update':
            sql = self.backend.sql_create_function_update(fname,
                                                          column,
                                                          tname,
                                                          action)
        elif action == 'delete':
            sql = self.backend.sql_create_function_delete(fname,
                                                          column,
                                                          tname,
                                                          action)
        else:
            raise ActionUnknown(Exception)

        return sql

    def drop_triggers(self, name):
        for sql in self.sql_drop_triggers(name):
            pgcommands.execute_raw(sql, self.database)


    def sql_drop_triggers(self, table):
        """DROP triggers

        table (string) : the table name
        """
        sql = []
        for action in self.ACTIONS:
            sql.append(self.sql_drop_trigger(trigger_name(table, action),
                                             table))
        return sql


    def sql_drop_function(self, name):
        """Return SQL statement build by the backend
        """
        return self.backend.sql_drop_function(name)

    def sql_drop_trigger(self, name, table):
        """Return SQL statement build by the backend
        """
        return self.backend.sql_drop_trigger(name, table)

    def sql_drop_table(self, name):
        """Return SQL statement build by the backend
        """
        return self.backend.sql_drop_table(name)


def command_check():
    """
    Check indexes
    """
    for fpath in get_app_paths():
        print fpath

def get_app_paths():
    """
    Return all paths defined in settings
    """
    trigg = []
    for model in get_models():
        for field in model._meta.fields:
            if str(field.__class__) == "<class 'foo.aggtrigg.models.IntegerTriggerField'>":
                trigg.append({"model": model,
                              "table": model._meta.db_table,
                              "field": field.name,
                              "aggs": field.aggregate_trigger})

    return trigg
