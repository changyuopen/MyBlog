# -*- coding: utf-8 -*-

'''
Created on 2014???10???25???

@author: changyuopen
'''

from DBManager import DBManager


class DBHelper:
    
    @staticmethod
    def execute(sql, param=None):
        db = DBManager.getConnection()
        cursor = db.cursor()
        count = 0
        try:
            if param == None or param == ():
                count = cursor.execute(sql)
            else:
                count = cursor.execute(sql, param)
            db.commit()
        except:
            db.rollback()
        db.close()
        return count
    
    @staticmethod
    def select(sql, param=None):
        db = DBManager.getConnection()
        cursor = db.cursor()
        result = None
        try:
            if param == None or param == ():
                cursor.execute(sql)
            else:
                cursor.execute(sql, param)
            result = cursor.fetchall()
        except:
            print "select error"
        db.close()
        return result
    
            
        
        
        
    
    
    
    
