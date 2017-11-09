# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyodbc
import urllib
import datetime

def updatas(datas):
    DBfile = ur"D:/Python/sunyx/access/cache-收益率曲线明细数据（历史）.mdb"
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

datas = []

username = "dybond"
function_id = "106015"
function_name = u"收益率曲线明细数据"
func_id = "2011"
style_type = "90"
periodicity = "0"
periods = "m"
p_qxmc_list = [
    u"中债城投债收益率曲线(AA(2))",
    u"中债城投债收益率曲线(AA)",
    u"中债城投债收益率曲线(AA-)",
    u"中债城投债收益率曲线(AAA)",
    u"中债城投债收益率曲线(AA＋)",
    u"中债地方政府债收益率曲线(AAA)",
    u"中债地方政府债收益率曲线(AAA-)",
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
    u"中债浮动利率中短期票据(SHIBOR-1Y-20D)点差曲线(AAA)",
    u"中债浮动利率中短期票据(SHIBOR-1Y-20D)点差曲线(AA＋)",
    u"中债浮动利率资产支持证券(Depo-1Y)点差曲线(A)",
    u"中债浮动利率资产支持证券(Depo-1Y)点差曲线(AA)",
    u"中债浮动利率资产支持证券(Depo-1Y)点差曲线(AAA)",
    u"中债浮动利率资产支持证券(R07D-1M)点差曲线(AAA)",
    u"中债国开债收益率曲线",
    u"中债国债收益率曲线",
    u"中债进出口行债收益率曲线",
    u"中债农发行债收益率曲线",
    u"中债企业债收益率曲线(A)",
    u"中债企业债收益率曲线(A-)",
    u"中债企业债收益率曲线(AA)",
    u"中债企业债收益率曲线(AA-)",
    u"中债企业债收益率曲线(AAA)",
    u"中债企业债收益率曲线(AAA-)",
    u"中债企业债收益率曲线(AA＋)",
    u"中债企业债收益率曲线(A＋)",
    u"中债企业债收益率曲线(B)",
    u"中债企业债收益率曲线(BB)",
    u"中债企业债收益率曲线(BBB)",
    u"中债企业债收益率曲线(BBB＋)",
    u"中债企业债收益率曲线(CC)",
    u"中债企业债收益率曲线(CCC)",
    u"中债商业银行次级债收益率曲线(A)(已停编)",
    u"中债商业银行次级债收益率曲线(A-)(已停编)",
    u"中债商业银行次级债收益率曲线(AA)(已停编)",
    u"中债商业银行次级债收益率曲线(AA-)(已停编)",
    u"中债商业银行次级债收益率曲线(AAA)(已停编)",
    u"中债商业银行次级债收益率曲线(AA＋)(已停编)",
    u"中债商业银行次级债收益率曲线(A＋)(已停编)",
    u"中债商业银行次级债收益率曲线(BBB＋)(已停编)",
    u"中债商业银行普通债收益率曲线(A)",
    u"中债商业银行普通债收益率曲线(A-)",
    u"中债商业银行普通债收益率曲线(AA)",
    u"中债商业银行普通债收益率曲线(AA-)",
    u"中债商业银行普通债收益率曲线(AAA)",
    u"中债商业银行普通债收益率曲线(AAA-)",
    u"中债商业银行普通债收益率曲线(AA＋)",
    u"中债商业银行普通债收益率曲线(A＋)",
    u"中债铁道债收益率曲线",
    u"中债铁道债收益率曲线(减税)",
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
    u"中债资产支持证券收益率曲线(AA)",
    u"中债资产支持证券收益率曲线(AA-)",
    u"中债资产支持证券收益率曲线(AAA)",
    u"中债资产支持证券收益率曲线(AAA-)",
    u"中债资产支持证券收益率曲线(AA＋)",
    u"中债资产支持证券收益率曲线(A＋)"
]
p_step_list = [
    "0.2",
    "0.1",
    "0.5",
    "1"
]

n = 1
begin = datetime.date(2002,1,4)
end = datetime.date(2017,3,13)
for i in range((end - begin).days+1):
    day = begin + datetime.timedelta(days=i)
    p_startdate = str(day).replace("-","")
    for p_qxmc in p_qxmc_list:
        p_qxmc_urlcode =  urllib.quote(p_qxmc.encode('gbk'))
        for p_step_l in p_step_list:
            params = "function_id=106015&p_startdate=" + p_startdate + "&p_qxmc=" + p_qxmc_urlcode + "&p_qxfl=&p_step=" + p_step_l + "&p_flag_year=1"
            paramstext = u"开始日期:" + p_startdate + u" 曲线名称:" + p_qxmc + u" 计算步长（年）:" + p_step_l
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
            if len(datas) >= 1000:
                updatas(datas)
                datas = []
                print n
            n = n +1

updatas(datas)
