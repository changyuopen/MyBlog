# -*- coding: utf-8 -*-

'''
Created on 2014???10???25???

@author: changyuopen
'''

from dataaccess.core import dbmanager


def execute(sql, param=None):
    db = dbmanager.getConnection()
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
    
def select(sql, param=None):
    db = dbmanager.getConnection()
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
    
            
        
        
        
    
    
    
    
