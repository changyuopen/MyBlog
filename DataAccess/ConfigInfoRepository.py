# -*- coding: utf-8 -*-

'''
Created on 2014年10月25日

@author: changyuopen
'''
from Core.DBHelper import DBHelper
from Domain.ConfigInfo import ConfigInfo
    
class ConfigInfoRepository:
    
    def getAllConfigInfo(self):
        sql = "select * from configinfo;"
        result = DBHelper.select(sql)
        items = []
        for row in result:
            tmp = ConfigInfo(row["ID"], row["Name"], row["Value"], row["Type"])
            items.append(tmp)
        return list
    
    def updateConfigInfo(self, configInfo):
        sql = """update configinfo set Name = %s, Value = %s, Type = %s
where ID=%s """
        param = (configInfo.getName(), configInfo.getValue(), configInfo.getType(),
                 configInfo.getId())
        count = DBHelper.execute(sql, param)
        return count
        


    
    
        
            
            
        
        
        
