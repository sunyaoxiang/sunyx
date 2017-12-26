# coding: utf-8
import io;
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
import json

a = io.open("user.txt", encoding="utf8")
for i in a:
    i = i.replace("\r", "")
    i = i.replace("\n", "")
    try:
        try:
            t = json.loads(i)
            print str(t['minThresholdValue']) + "|" + str(t["maxThresholdValue"]) + "|" + t["emailUsr"]
        except:
            print str(t['params'][0]['min']) + "|" + str(t['params'][0]['max']) + "|" + t["emailUsr"]
    except:
        print "" + "|" + "" + "|" + t["emailUsr"]

'''SELECT
	t.TASK_GROUP,
	t.TASK_NAME,
	r.cron,
	m.own_by,
	t.TASK_PARAMS
FROM
	task_detail t,
	task_trigger r,
	m_monitor m
WHERE
	r.job_id = t.ID
AND
m.name_cn = t.TASK_NAME
AND t.TASK_GROUP IN (
	"153_datayesdb",
	"153_datayesdbp",
	"153_datayesdb_mysql",
	"72_datayesdb",
	"72_spiderdb",
	"72库表",
	"73_datayesdb",
	"api-上市公司",
	"api-上市公司-v1",
	"api-债券信息",
	"api-债券信息-v1",
	"api-债券信息=v1",
	"api-公司资料",
	"api-公司资料-v1",
	"api-基本面数据",
	"api-基本面数据-v1",
	"api-基金信息",
	"api-基金信息-v1",
	"api-宏观行业",
	"api-宏观行业-v1",
	"api-市场行情数据",
	"api-市场行情数据-v1",
	"api-常量",
	"api-常量-v1",
	"api-报告相关",
	"api-报告相关-v1",
	"api-指数信息",
	"api-指数信息-v1",
	"api-期货",
	"api-期货-v1",
	"api-期货信息",
	"api-期货信息-v1",
	"api-沪深股票信息",
	"api-沪深股票信息-v1",
	"api-沪港通",
	"api-沪港通-v1",
	"api-港股信息",
	"api-港股信息-v1",
	"api-特色大数据",
	"api-特色大数据-v1",
	"api-私募基金",
	"api-私募基金-v1",
	"api-简单",
	"api-证券概况",
	"api-证券概况-v1",
	"api简-宏观行业",
	"api简-宏观行业-v1",
	"api简单监控",
	"api简单监控-v1",
	"big_data",
	"http定时执行",
	"md_inst_rating",
	"news-db",
	"news-db01",
	"sh-datamall-db02",
	"sh-dm-db01",
	"sh-dm-db02",
	"sh-inv-db02-qa",
	"sh-inv-db03",
	"sh-inv-db03-qa",
	"sql定时执行",
	"sql定时执行-72_datayesdb",
	"vip-newapi-wmcloud-com/v1/api/consensus/",
	"vip-newapi-wmcloud-com/v1/api/equity/",
	"vip-newapi-wmcloud-com/v1/api/listedCorp/",
	"vip-newapi-wmcloud-com/v1/api/macro/",
	"vip_newapi_wmcloud_com/v1/api/equity/",
	"vip_newapi_wmcloud_com/v1/api/fund/",
	"vip_newapi_wmcloud_com/v1/api/options/",
	"数据库表全量监控",
	"数据表增量监控",
	"监控平台数据监控",
	"股吧发帖数每日入库监控",
	"雪球发帖数每日入库监控"
) -- GROUP BY
--  t.TASK_GROUP
ORDER BY
	t.TASK_GROUP,
	t.TASK_NAME '''