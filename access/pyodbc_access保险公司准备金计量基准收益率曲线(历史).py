# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyodbc
import urllib
import datetime


datas = []

username = "dybond"
function_id = "106016"
function_name = u"保险公司准备金计量基准收益率曲线"
func_id = "2011"
style_type = "90"
periodicity = "0"
periods = "m"

n = 1
begin = datetime.date(2002,1,4)
end = datetime.date(2017,3,13)
for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)
    strday = str(day).replace("-","")
    params = "function_id=106016&p_in_date=" + strday + "&p_in_days=750&p_flag_year=1"
    paramstext = u"日期:" + strday + u" 平均日天数:750"
    datas.append({
        "id":str(n),
        "username":username,
        "function_id":function_id,
        "function_name":function_name,
        "func_id":func_id,
        "style_type":style_type,
        "params":params,
        "paramstext":paramstext,
        "periodicity":periodicity,
        "periods":periods,
    })
    n = n +1


DBfile = ur"D:/Python/sunyx/access/cache-保险公司准备金计量基准收益率曲线(历史).mdb"
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;",charset="utf8")
cursor = conn.cursor()
for dat in datas:
    SQL = '''Insert INTO [excelparams] (\
    id,\
    username,\
    function_id,\
    function_name,\
    func_id,\
    style_type,\
    params,\
    paramstext,\
    periodicity,\
    periods,\
    beginTime,\
    function_url,\
    paramsurl,\
    filename\
    ) \
    VALUES \
    (?,\
    ?,\
    ?,\
    ?,\
    ?,\
    ?,\
    ?,\
    ?,\
    ?,\
    ?,\
    '2017/3/15 11:01:00',\
    '',\
    '',\
    ''\
    ) '''
    selsql = (
        dat["id"],
        dat["username"],
        dat["function_id"],
        dat["function_name"],
        dat["func_id"],
        dat["style_type"],
        dat["params"],
        dat["paramstext"],
        dat["periodicity"],
        dat["periods"]
    )
    # print selsql
    # print SQL
    cursor.execute(SQL,selsql)
cursor.commit()
cursor.close()
conn.close()
