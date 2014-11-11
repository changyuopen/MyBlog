# -*- coding: utf-8 -*-

'''
Created on 2014年10月25日

@author: changyuopen
'''
from dataaccess.core import dbhelper
from domain.configinfo import ConfigInfo
    
class ConfigInfoRepository:
    
    def getAllConfigInfo(self):
        sql = "select * from configinfo;"
        result = dbhelper.select(sql)
        items = []
        for row in result:
            tmp = ConfigInfo(row["ID"], row["Name"], row["Value"], row["Type"])
            items.append(tmp)
        return items
    
    def updateConfigInfo(self, configInfo):
        sql = """update configinfo set Name = %s, Value = %s, Type = %s
where ID=%s """
        param = (configInfo.getName(), configInfo.getValue(), configInfo.getType(),
                 configInfo.getId())
        count = dbhelper.execute(sql, param)
        return count
        


    
    
        
            
            
        
        
        
