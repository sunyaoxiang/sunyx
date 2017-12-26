# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import pyodbc
import urllib
import datetime


datas = [

]

idoks_list = datas

mdb_name = ur"cache-中债指数样本券数据(当年)_20171018_4"
DBfile = ur"D:/Python/sunyx/access/" + mdb_name + ".mdb"
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;",
                      charset="utf8")
cursor = conn.cursor()
for idoks in idoks_list:
    SQL = '''DELETE FROM [excelparams] WHERE ID = ? '''
    sqlvalues = (
        idoks
    )
    # print selsql
    # print SQL
    cursor.execute(SQL, sqlvalues)
cursor.commit()
cursor.close()
conn.close()
