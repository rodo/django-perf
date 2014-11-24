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

from jinja2 import Environment, FileSystemLoader
import os

BIGINT = "int4"

class TriggerPostgreSQL(object):

    def __init__(self):
        self.name = "PostgreSQL"

    def sql_create_table(self, name, column, aggregats):
        """Return a SQL statement to create a FUNCTION
        
        name : functions name
        column : column name
        aggregats (array): aggregats used
        """
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    
        template = env.get_template('pg_create_table.sql')
        aggs = []
        for agg in aggregats:
            aggs.append({"name": agg,
                         "type": BIGINT})
        
        return template.render(name=name,
                               column={"name": column, "type": BIGINT},
                               aggregats=aggs)

    def sql_drop_table(self, name):
        """Return a command to drop a table in PostgreSQL

        name (string) : the table name
        """
        return "DROP TABLE IF EXISTS {0}".format(name)

    def sql_drop_trigger(self, name, table):
        """Return a command to drop a trigger in PostgreSQL

        name (sttring): the triggers's name
        table (string) : the table name
        """
        return "DROP TRIGGER IF EXISTS {0} ON {1}".format(name, table)

    def sql_drop_function(self, name):
        """Return a command to drop a function in PostgreSQL
        
        name (string): the function's name to drop
        """
        return "DROP FUNCTION IF EXISTS {0}".format(name)

    def sql_create_trigger(self, name, function, table, action):
        """Return a command to create a trigger in PostgreSQL
        
        name (string): the function's name to drop
        """
        return """CREATE TRIGGER {0} AFTER {3} ON {2}
        FOR EACH ROW
        EXECUTE PROCEDURE {1}""".format(name, function, table, action.upper())

    def sql_create_function_insert(self, name, table, column, aggtable):
        """Return a SQL statement to create a FUNCTION
        
        name : function name
        table (string) : the originate of datas
        column : column name
        aggtable : the table where data will be stored
        """
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__),
                                                               'templates')))
    
        template = env.get_template('pg_function_insert.sql')

        actions = "agg_count=agg_count+1"
        
        return template.render(name=name,
                               table=table,
                               aggtable=aggtable,
                               column=column,
                               actions=actions)

    def sql_create_function_delete(self, name, column, aggtable, action):
        """Return a SQL statement to create a FUNCTION
        
        name : functions name
        column : column name
        aggtable : the table where data will be stored
        action : action that fired the trigger
        """
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    
        template = env.get_template('pg_function_delete.sql')

        actions = "agg_count=agg_count-1"
        
        return template.render(name=name,
                               table=aggtable,
                               column=column,
                               actions=actions)

    def sql_create_function_update(self, name, column, aggtable, action):
        """Return a SQL statement to create a FUNCTION
        
        name : functions name
        column : column name
        aggtable : the table where data will be stored
        action : action that fired the trigger
        """
        env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    
        template = env.get_template('pg_function_update.sql')

        actions_new = "agg_count=agg_count+1"
        actions_old = "agg_count=agg_count-1"
        
        return template.render(name=name,
                               table=aggtable,
                               column=column,
                               actions_old=actions_old,
                               actions_new=actions_new)





