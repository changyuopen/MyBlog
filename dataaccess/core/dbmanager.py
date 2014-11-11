# -*- coding: utf-8 -*-

'''
Created on 2014???10???25???

@author: changyuopen
'''

import MySQLdb
import MySQLdb.cursors

from dataaccess.core import dbinfo


def getConnection():
    return MySQLdb.connect(host=dbinfo.server, user=dbinfo.user, passwd=dbinfo.pwd,
                           db=dbinfo.dbname, charset=dbinfo.charset, 
                           cursorclass=MySQLdb.cursors.DictCursor)
