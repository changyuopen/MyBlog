# -*- coding: utf-8 -*-

from dataaccess import configinfo

obj = configinfo()
items = obj.getAllConfigInfo()
for item in items:
    print item.getName()

