# -*- coding: utf-8 -*-

'''
Created on 2014???10???25???

@author: changyuopen
'''

import MySQLdb
import MySQLdb.cursors

from DBInfo import DBInfo


class DBManager:
    
    @staticmethod
    def getConnection():
        return MySQLdb.connect(host=DBInfo.Server, user=DBInfo.User, passwd='', db='MyBlog', charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
