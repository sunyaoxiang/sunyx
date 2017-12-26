# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import pypyodbc
import urllib
import datetime
import os, traceback


def database_create(DBfile):
    try:
        if os.path.exists(DBfile) == False:
            pypyodbc.win_create_mdb(DBfile)
            conn = pypyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;",
                                    charset="utf8")
            cur = conn.cursor()
            sql1 = '''CREATE TABLE ''' + "excelparams" + '''(\
            ID Text PRIMARY KEY,\
            username Text,\
            function_id Text,\
            function_name Text,\
            func_id Text,\
            style_type Text,\
            params Text,\
            paramstext Text,\
            periodicity Int,\
            periods Text,\
            beginTime DATETIME,\
            function_url Text,\
            paramsurl Text,\
            filename Text\
            );'''
            sql2 = '''CREATE TABLE ''' + "tasklist" + '''(\
            ID Text,\
            execute_date Int ,\
            execute_flag Int,\
            error_flag Int,\
            PRIMARY KEY(ID,execute_date)
            );'''
            cur.execute(sql1)
            cur.execute(sql2)
            cur.commit()
            conn.close()
    except Exception, e:
        print e


for year in range(2017, 2018):
    for month in range(1, 5):
        try:
            datas = []
            n = 1
            # year = 2015
            # month = 1
            DBfile = ur"D:/Python/sunyx/access/cache-中债指数样本券数据(历史)_" + str(year) + "_" + str(month) + ".mdb"
            database_create(DBfile)
        except Exception, error:
            print error