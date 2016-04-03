#!/usr/bin/python
# coding: utf-8
"""
db.py - generic database classes
"""
from __future__ import division
import os
import sys
import warnings
import re
import csv
import MySQLdb as mysql
from itertools import ifilter
from collections import defaultdict
from optparse import OptionParser

class Column(object):
    """Database Column"""
    
    def __init__( self, con, name ):
        self.name = name

    def dump( self ):
        print "\t\tcolumn=%s" % (self.name)

class Table(object):
    """Database Table"""

    def __init__( self, con, schema_name, table_name ):
        self.name = table_name
        self.columns = []
        cur = con.cursor( mysql.cursors.DictCursor )
        query = "SELECT TABLE_NAME, COLUMN_NAME "
        query += "FROM information_schema.COLUMNS "
        query += "WHERE (TABLE_SCHEMA = %s) "
        query += "AND (TABLE_NAME = %s) "
        cur.execute( query, (schema_name, table_name) )
        for row in cur:
            self.columns.append( Column( con, row['COLUMN_NAME'] ) )
        cur.close()

    def __len__( self ):
        return len(self.columns)

    def __getitem__( self, i ):
        return self.columns[i]

    def dump( self ):
        print "\ttable=%s" % (self.name)
        for column in self.columns:
            column.dump()


class Schema(object):
    """Database Schema"""

    def __init__( self, con, name ):
        self.name = name
        self.tables = []
        cur = con.cursor( mysql.cursors.DictCursor )
        query = "SELECT TABLE_SCHEMA, TABLE_NAME "
        query += "FROM information_schema.TABLES "
        query += "WHERE (TABLE_SCHEMA = %s) "
        cur.execute( query, (name,) )
        for row in cur:
            self.tables.append( Table( con, self.name, row['TABLE_NAME'] ) )
        cur.close()
    
    def __len__( self ):
        return len(self.tables)

    def __getitem__( self, i ):
        return self.tables[i]

    def filter( self ):
        self.tables[:] = ifilter( lambda table: raw_input( "Keep %s y/N: " % table.name ) in 'Yy', self.tables )

    def dump( self ):
        print "schema=%s" % (self.name)
        for table in self.tables:
            table.dump()


                                

