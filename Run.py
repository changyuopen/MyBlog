# -*- coding: utf-8 -*-

# My Program
# from flask import Flask
# from view.index import *

# app = Flask(__name__)


# if __name__ == '__main__':
#    app.run()
from dataaccess import *
import MySQLdb

db = MySQLdb.connect(host=DBInfo.Server, user=DBInfo.User, passwd='', 
                     db='MyBlog', charset='utf8') 

cursor = db.cursor()
sql = """insert into configinfo (ID, Name, Value, Type)
values(uuid(), 'head','??????','system_config1');"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    
db.close()

# end

