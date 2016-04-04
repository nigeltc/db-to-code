#!/usr/bin/python
# coding: utf-8
"""
thing.py - thing
"""
from __future__ import division
import os
import sys
import warnings
import re
import csv
from itertools import ifilter
from collections import defaultdict

class Thing(object):
    ts = ['first', 'second', 'third', 'fourth', 'fifth']
    ti = 0

    @staticmethod
    def make_thing():
        name = Thing.ts[Thing.ti]
        Thing.ti = (Thing.ti + 1)%len(Thing.ts)
        return Thing( name )

    @staticmethod
    def make_things( n ):
        return [Thing.make_thing() for i in range(n)]

    def __init__( self, name ):
        self.name = name 

    def __str__( self ):
        return 'My name is %s' % (self.name)


if __name__ == '__main__':
    first = Thing.make_thing()
    print first
    second = Thing.make_thing()
    print second
    
    things = Thing.make_things( 6 )
    for thing in things:
        print thing


