# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import win32com.client

conn = win32com.client.Dispatch(r'ADODB.Connection')
DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=excelparams;'
conn.Open(DSN)
sql_statement = '''Insert INTO [excelparams] (username,function_id,function_name,func_id,style_type,params,paramstext,periodicity,periods,beginTime,function_url,paramsurl,filename) \
VALUES \
('dybond','106013','标准待偿期收益率曲线数据(历史)','2011,90','function_id=106013&p_startdate=TODAY&p_enddate=TODAY&p_qxmc=%D6%D0%D5%AE%B3%C7%CD%B6%D5%AE%CA%D5%D2%E6%C2%CA%C7%FA%CF%DF%28AA%282%29%29&p_qxfl=0&p_flag_year=1','开始日期:TODAY 结束日期:TODAY 曲线名称:中债城投债收益率曲线(AA(2)) 曲线类型:到期','1','M','2017/4/14 17:26:00','','','') '''

conn.Execute(sql_statement)
conn.Close()