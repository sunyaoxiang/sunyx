# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import pyodbc
import urllib
import datetime


datas = []

baseID = '10086'
username = "dybond"
function_id = "106013"
function_name = u"标准待偿期收益率曲线数据"
func_id = "2011"
style_type = "90"
periodicity = "0"
periods = "m"
p_qxmc_list = [
    # u"中债城投债收益率曲线(AA(2))",
    # u"中债城投债收益率曲线(AA)",
    # u"中债城投债收益率曲线(AA-)",
    # u"中债城投债收益率曲线(AAA)",
    # u"中债城投债收益率曲线(AA＋)",
    # u"中债地方政府债收益率曲线(AAA)",
    # u"中债地方政府债收益率曲线(AAA-)",
    u"中债浮动利率城投债(SHIBOR-1Y-10D)点差曲线(AA＋)",
    u"中债浮动利率企业债(Depo-1Y)点差曲线(AAA)",
    u"中债浮动利率企业债(R07D-2W)点差曲线(AAA)",
    u"中债浮动利率企业债(SHIBOR-1W-120D)点差曲线(AAA)",
    u"中债浮动利率企业债(SHIBOR-3M-5D)点差曲线(AAA)",
    u"中债浮动利率商业银行次级债(Depo-1Y)点差曲线(AA)(已停编)",
    u"中债浮动利率商业银行次级债(Depo-1Y)点差曲线(AAA)(已停编)",
    u"中债浮动利率商业银行次级债(Depo-1Y)点差曲线(AA＋)(已停编)",
    u"中债浮动利率商业银行普通债(Depo-1Y)点差曲线(AAA)",
    u"中债浮动利率商业银行普通债(SHIBOR-3M-1D)点差曲线(AAA-)",
    u"中债浮动利率商业银行普通债(SHIBOR-3M-1D)点差曲线(AA＋)",
    u"中债浮动利率政策性金融债(Depo-1Y)点差曲线",
    u"中债浮动利率政策性金融债(R07D-2W)点差曲线",
    u"中债浮动利率政策性金融债(SHIBOR-3M-5D)点差曲线",
    u"中债浮动利率中短期票据(Depo-1Y)点差曲线(AA)",
    u"中债浮动利率中短期票据(Depo-1Y)点差曲线(AA-)",
    u"中债浮动利率中短期票据(Depo-1Y)点差曲线(AAA)",
    u"中债浮动利率中短期票据(Depo-1Y)点差曲线(AA＋)",
    # u"中债浮动利率中短期票据(SHIBOR-1Y-20D)点差曲线(AAA)",
    # u"中债浮动利率中短期票据(SHIBOR-1Y-20D)点差曲线(AA＋)",
    u"中债浮动利率资产支持证券(Depo-1Y)点差曲线(A)",
    u"中债浮动利率资产支持证券(Depo-1Y)点差曲线(AA)",
    u"中债浮动利率资产支持证券(Depo-1Y)点差曲线(AAA)",
    u"中债浮动利率资产支持证券(R07D-1M)点差曲线(AAA)",
    # u"中债国开债收益率曲线",
    # u"中债国债收益率曲线",
    # u"中债进出口行债收益率曲线",
    # u"中债农发行债收益率曲线",
    # u"中债企业债收益率曲线(A)",
    # u"中债企业债收益率曲线(A-)",
    # u"中债企业债收益率曲线(AA)",
    # u"中债企业债收益率曲线(AA-)",
    # u"中债企业债收益率曲线(AAA)",
    # u"中债企业债收益率曲线(AAA-)",
    # u"中债企业债收益率曲线(AA＋)",
    # u"中债企业债收益率曲线(A＋)",
    u"中债企业债收益率曲线(B)",
    u"中债企业债收益率曲线(BB)",
    u"中债企业债收益率曲线(BBB)",
    # u"中债企业债收益率曲线(BBB＋)",
    u"中债企业债收益率曲线(CC)",
    u"中债企业债收益率曲线(CCC)",
    u"中债商业银行次级债收益率曲线(A)(已停编)",
    u"中债商业银行次级债收益率曲线(A-)(已停编)",
    # u"中债商业银行次级债收益率曲线(AA)(已停编)",
    # u"中债商业银行次级债收益率曲线(AA-)(已停编)",
    u"中债商业银行次级债收益率曲线(AAA)(已停编)",
    # u"中债商业银行次级债收益率曲线(AA＋)(已停编)",
    # u"中债商业银行次级债收益率曲线(A＋)(已停编)",
    # u"中债商业银行次级债收益率曲线(BBB＋)(已停编)",
    u"中债商业银行普通债收益率曲线(A)",
    u"中债商业银行普通债收益率曲线(A-)",
    # u"中债商业银行普通债收益率曲线(AA)",
    # u"中债商业银行普通债收益率曲线(AA-)",
    # u"中债商业银行普通债收益率曲线(AAA)",
    # u"中债商业银行普通债收益率曲线(AAA-)",
    # u"中债商业银行普通债收益率曲线(AA＋)",
    # u"中债商业银行普通债收益率曲线(A＋)",
    # u"中债铁道债收益率曲线",
    # u"中债铁道债收益率曲线(减税)",
    u"中债央行票据收益率曲线",
    u"中债中短期票据收益率曲线(A)",
    u"中债中短期票据收益率曲线(A-)",
    u"中债中短期票据收益率曲线(AA)",
    u"中债中短期票据收益率曲线(AA-)",
    u"中债中短期票据收益率曲线(AAA)",
    u"中债中短期票据收益率曲线(AAA-)",
    u"中债中短期票据收益率曲线(AAA＋)",
    u"中债中短期票据收益率曲线(AA＋)",
    u"中债中短期票据收益率曲线(A＋)",
    # u"中债资产支持证券收益率曲线(AA)",
    # u"中债资产支持证券收益率曲线(AA-)",
    # u"中债资产支持证券收益率曲线(AAA)",
    # u"中债资产支持证券收益率曲线(AAA-)",
    u"中债资产支持证券收益率曲线(AA＋)",
    # u"中债资产支持证券收益率曲线(A＋)"
]
p_qxfl_list = [
    ["0", u"到期"],
    ["1", u"即期"],
    ["2", u"远期的到期(N=1)"],
    ["3", u"远期的到期(N=2)"],
    ["4", u"远期的到期(N=3)"],
    ["5", u"远期的到期(N=4)"],
    ["6", u"远期的到期(N=5)"],
    ["7", u"远期的到期(K=1)"],
    ["8", u"远期的到期(K=2)"],
    ["9", u"远期的到期(K=3)"],
    ["10", u"远期的到期(K=4)"],
    ["11", u"远期的到期(K=5)"],
    ["12", u"远期的即期(N=1)"],
    ["13", u"远期的即期(N=2)"],
    ["14", u"远期的即期(N=3)"],
    ["15", u"远期的即期(N=4)"],
    ["16", u"远期的即期(N=5)"],
    ["17", u"远期的即期(K=1)"],
    ["18", u"远期的即期(K=2)"],
    ["19", u"远期的即期(K=3)"],
    ["20", u"远期的即期(K=4)"],
    ["21", u"远期的即期(K=5)"]
]

# begin = datetime.date(2014,6,1)
# end = datetime.date(2014,6,7)
# for i in range((end - begin).days+1):
# day = begin + datetime.timedelta(days=i)
#         strday = str(day).replace("-","")
n = 1000
for p_qxmc in p_qxmc_list:
    for p_qxfl_l in p_qxfl_list:
        p_qxmc_urlcode = urllib.quote(p_qxmc.encode('gbk'))
        params = "function_id=106013&p_startdate=20020104&p_enddate=20150313&p_qxmc=" + p_qxmc_urlcode + "&p_qxfl=" + \
                 p_qxfl_l[0] + "&p_flag_year=1"
        paramstext = u"开始日期:20020104 结束日期:20150313 曲线名称:" + p_qxmc + u" 曲线类型:" + p_qxfl_l[1]
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
        n = n + 1

DBfile = ur"D:/Python/sunyx/access/cache-标准待偿期收益率曲线数据-14k.mdb"
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
    cursor.execute(SQL, selsql)
cursor.commit()
cursor.close()
conn.close()
