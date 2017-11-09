#coding=utf-8
import urllib,urllib2,re
import lxml
from lxml import html
from lxml import etree
import MySQLdb
import datetime


now = datetime.datetime.now()

urllist = []
url = 'http://www.douguo.com/top/remenyonghu/'
urllist.append(url)
for i in [30,60,90]:
    url = 'http://www.douguo.com/top/remenyonghu/'
    url = url + '/'+str(i)
    #print url
    urllist.append(url)

    # def do_job(self):
    #     res = []
    #     for day in self.days:
    #         for cur in self.currency:
    #             url = self.__geturl(cur,day)
    #             content = http_request.do_get(url)
    #             htmlSource = HTML.fromstring(content)
    #             xpath = '''//*[@id="ratesTable"]/tbody/tr'''
    #             tree = htmlSource.xpath(xpath)
    #             for idx,tr in enumerate(tree):
    #                 content = ETree.tostring(tr)
    #                 htmltmp = HTML.fromstring(content)
    #                 ticker = htmltmp.xpath("//td[1]/span")[0].text.strip()
    #                 val = float(htmltmp.xpath("//td[3]")[0].text.strip())
    #                 date_ = datetime.strptime(day,"%Y%m%d").strftime("%Y-%m-%d")
    #                 record = {"TRADE_DATE":date_ , "CURRENCY":cur, "TICKER_SYMBOL":ticker,"VALUE":val }
    #                 res.append(record)
    #         if len(res) > 100:
    #             update2db(res, self.datadb)
    #             res = []
    #     update2db(res, self.datadb)

for u in urllist:
    request = urllib2.Request(u)
    request.add_header('Cache-Control', 'max-age=0')
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
    request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    response = urllib2.urlopen(request).read()
    #print response
    htmlSource = etree.HTML(response)
    # tree = htmlSource.xpath('''.//*[@id='main']/div[2]/div[1]/ul/li/a[1]''')
    # #tree = htmlSource.xpath('//a')
    # #print tree
    # for i in tree:
    #     print i.attrib['title'],i.attrib['href']

    tree = htmlSource.xpath('''.//*[@id='main']/div[2]/div[1]/ul/li''')
    print tree