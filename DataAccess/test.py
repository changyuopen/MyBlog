# -*- coding: utf-8 -*-

from ConfigInfoRepository import ConfigInfoRepository

obj = ConfigInfoRepository()
items = obj.getAllConfigInfo()
for item in items:
    print item.getName()

