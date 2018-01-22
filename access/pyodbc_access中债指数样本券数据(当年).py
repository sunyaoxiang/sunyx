# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import pyodbc
import urllib
import datetime


def updatas(datas, DBfile):
    # DBfile = ur"D:/Python/sunyx/access/cache-中债指数样本券数据(历史).mdb"
    conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;",
                          charset="utf8")
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
        '2017/9/26 10:01:00',\
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
        cursor.execute(SQL, selsql)
    cursor.commit()
    cursor.close()
    conn.close()


username = "dybond"
function_id = "10702"
function_name = u"中债指数样本券数据(当年)"
func_id = "2011"
style_type = "90"
periodicity = "0"
periods = "m"

p_termtype_list = [
    [u"总值", "0"],
    [u"1年以下", "1"],
    [u"1-3年", "2"],
    [u"3-5年", "3"],
    [u"5-7年", "4"],
    [u"7-10年", "5"],
    [u"10年以上", "6"],
]

for year in range(2017, 2018):
    for month in range(1, 5):
        try:
            datas = []
            n = 1
            # year = 2015
            # month = 1
            DBfile = ur"D:/Python/sunyx/access/cache-中债指数样本券数据(当年)_" + str(year) + "_" + str(month) + ".mdb"
            print DBfile
            begin = datetime.date(year, month, 1)
            if month != 12:
                end = datetime.date(year, month + 1, 1)  # 2017,3,13
            else:
                end = datetime.date(year + 1, 1, 1)  # 2017,3,13
            print begin
            print end
            for i in range((end - begin).days):
                day = begin + datetime.timedelta(days=i)
                p_sdate = str(day).replace("-", "")
                # for p_qxmc in p_qxmc_list:
                # p_qxmc_urlcode =  urllib.quote(p_qxmc.encode('gbk'))
                for p_termtype in p_termtype_list:
                    params = "function_id=10702&p_indextype=&p_termtype=" + p_termtype[
                        1] + "&p_sdate=" + p_sdate + "&p_in_queryyear=0"
                    paramstext = u"待偿期限:" + p_termtype[0] + u" 采样日期:" + p_sdate
                    datas.append({
                        "id": str(n),
                        "username": username,
                        "function_id": function_id,
                        "function_name": function_name,
                        "func_id": func_id,
                        "style_type": style_type,
                        "params": params,
                        "paramstext": paramstext,
                        "periodicity": periodicity,
                        "periods": periods,
                    })
                    # if len(datas) >= 100:
                    # updatas(datas,DBfile)
                    #     datas = []
                    #     print n
                    n = n + 1

            updatas(datas, DBfile)
        except Exception, error:
            print error
