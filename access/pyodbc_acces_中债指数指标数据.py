# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyodbc
import urllib
import datetime

def updatas(datas,DBfile):
    # DBfile = ur"D:/Python/sunyx/access/cache-中债指数样本券数据(历史).mdb"
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
        '2017/3/22 10:01:00',\
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



username = "dybond"
function_id = "107012"
function_name = u"中债指数指标数据(历史)"
func_id = "2011"
style_type = "90"
periodicity = "0"
periods = "m"

p_termtype_list = [
    [u"总值","0"],
    [u"1年以下","1"],
    [u"1-3年","2"],
    [u"3-5年","3"],
    [u"5-7年","4"],
    [u"7-10年","5"],
    [u"10年以上","6"],
]


n = 1
datas = []
for year in range (2002,2018):
    try:
        DBfile = ur"D:/Python/sunyx/access/cache-中债指数指标数据20170824.mdb"
        print DBfile
        for p_termtype in p_termtype_list:
            params = "function_id=107012&p_startdate=" + str(year) + "0101&p_enddate=" + str(year) + "1231&p_indextype=&p_termtype=" + p_termtype[1] + "&p_in_queryyear=1"
            paramstext = u"开始日期:" + str(year) + u"0101 结束日期:" + str(year) + u"1231 待偿期限:"+ p_termtype[0]
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
            # if len(datas) >= 100:
            #     updatas(datas,DBfile)
            #     datas = []
            #     print n
            n = n +1
        updatas(datas,DBfile)
        datas = []
    except Exception,error:
        print error
