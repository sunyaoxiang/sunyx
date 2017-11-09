#coding=utf-8
'''
from yaoxiang.sun
'''
import urllib,urllib2,re
import lxml
from lxml import html
from lxml import etree as Etree
import MySQLdb
import datetime
import sys
type = sys.getfilesystemencoding()   # 关键

now = datetime.datetime.now()

urllist = []
#url = 'http://info.stcn.com/companydata/parOtherListedCompany.jsp?currentPage=2&startYear=2015&startMonth=03-31&issort=qmcgbl&ASCFlag=1'
url = 'http://info.stcn.com/companydata/parOtherListedCompany.jsp'

def getdata(startyear,startmonth,currentPage):
    for currentPage_i in range(1,currentPage):
        values = {'startYear':startyear,
                    'startMonth':startmonth,
                    'listedSelect':'0',
                    'industrySelect':'0',
                    'zoneSelect':'0',
                    'exponentSelect':'0',
                    'Submit.x':'33',
                    'Submit.y':'11',
                    'currentPage':currentPage_i}
        #print values['startYear'],values['startMonth']
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        req.add_header('Cache-Control', 'max-age=0')
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
        req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        req.add_header('Content-Type','application/x-www-form-urlencoded')
        response = urllib2.urlopen(req).read().decode("GBK")
        htmlSource = Etree.HTML(response)
        tree2 = htmlSource.xpath('''.//*[@id='detail']/table/tr[position()>2]''')
        for tr2 in tree2:
            TICKER_SYMBOL = tr2.xpath('.//td[1]')[0].text.strip()#股票代码
            SEC_SHORT_NAME = tr2.xpath('.//td[2]')[0].text.strip()#股票简称
            TAKE_TICKER_SYMBOL = tr2.xpath('.//td[3]')[0].text.strip()#持有对象代码
            TAKE_SEC_SHORT_NAME = tr2.xpath('.//td[4]')[0].text.strip()#持有对象简称
            INI_INVEST_AMOUNT = tr2.xpath('.//td[5]')[0].text.strip()#初始投资金额(万元)
            HOLDING_RATIO = tr2.xpath('.//td[6]')[0].text.strip()	#持股比例(%)
            END_ACCOUNTING_VALUE = tr2.xpath('.//td[7]')[0].text.strip()	#期末账面价值(万元)
            REPORTING_PROFIT = tr2.xpath('.//td[8]')[0].text.strip()	#报告期损益(万元)
            SOURCE_URL = tr2.xpath('.//td[2]/a')[0].attrib['href'].strip() #源网页地址
            END_DATE = values['startYear']+'-'+values['startMonth']

            print TICKER_SYMBOL,SEC_SHORT_NAME,END_DATE,TAKE_TICKER_SYMBOL,TAKE_SEC_SHORT_NAME,INI_INVEST_AMOUNT,HOLDING_RATIO,END_ACCOUNTING_VALUE,REPORTING_PROFIT,SOURCE_URL

req = urllib2.Request(url)
req.add_header('Cache-Control', 'max-age=0')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
req.add_header('Content-Type','application/x-www-form-urlencoded')
response = urllib2.urlopen(req).read().decode("GBK")
htmlSource = Etree.HTML(response)

startYear = []
tree = htmlSource.xpath('''.//*[@id='startYear']/option[position()>1]''')
for i in tree:
    startYear.append(i.text.strip())

startMonth = []
tree = htmlSource.xpath('''.//*[@id='startMonth']/option[position()>1]''')
for i in tree:
    startMonth.append(i.text.strip())

for startyear in startYear:
    for startmonth in startMonth:
        values = {'startYear':startyear,
                    'startMonth':startmonth,
                    'listedSelect':'0',
                    'industrySelect':'0',
                    'zoneSelect':'0',
                    'exponentSelect':'0',
                    'Submit.x':'33',
                    'Submit.y':'11',
                    'currentPage':1}
        #print values['startYear'],values['startMonth']
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        req.add_header('Cache-Control', 'max-age=0')
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
        req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        req.add_header('Content-Type','application/x-www-form-urlencoded')
        response = urllib2.urlopen(req).read().decode("GBK")
        htmlSource = Etree.HTML(response)
        lastpage = htmlSource.xpath('''.//*[@id='detail']/div/div/a[2]''')
        if lastpage == []:
            currentPage = 0
        else:
            hreftext = r'/companydata/parOtherListedCompany.jsp\?currentPage=(\d*)&startYear'
            hrefbase = lastpage[0].attrib['href']
            #print hrefbase
            currentPage = re.findall(re.compile(hreftext),hrefbase)[0]
            #print startyear,startmonth,currentPage
            getdata(startyear,startmonth,int(currentPage))

