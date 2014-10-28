# -*- coding: utf-8 -*-
'''
Created on 2014年10月25日

@author: changyuopen
'''

class ConfigInfo:
    
    def __init__(self, _id, _name, _value, _type):
        self.__id = _id
        self.__name = _name
        self.__value = _value
        self.__type = _type
        
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value
    
    def getType(self):
        return self.__type
    

        