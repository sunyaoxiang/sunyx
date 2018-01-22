# coding=utf-8
import urllib, urllib2, re
import lxml
from lxml import html
from lxml import etree
import MySQLdb
import datetime


now = datetime.datetime.now()

urllist = []
url = 'http://www.douguo.com/top/remenyonghu/'
urllist.append(url)
for i in [30, 60, 90]:
    url = 'http://www.douguo.com/top/remenyonghu/'
    url = url + '/' + str(i)
    # print url
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
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
    request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    response = urllib2.urlopen(request).read()
    # print response
    htmlSource = etree.HTML(response)
    # tree = htmlSource.xpath('''.//*[@id='main']/div[2]/div[1]/ul/li/a[1]''')
    # #tree = htmlSource.xpath('//a')
    # #print tree
    # for i in tree:
    #     print i.attrib['title'],i.attrib['href']

    tree = htmlSource.xpath('''.//*[@id='main']/div[2]/div[1]/ul/li''')
    #tree = htmlSource.xpath('//a')
    for i in tree:
        ixpath = i.xpath('.//a')[0]

        name = ixpath.attrib['title']
        #print i.xpath('./div')[0].text

        funs = i.xpath('./div')[0].text
        # fan_nums = ur'(\d*)粉丝'#get uid
        fan_nums = ur'(\d*)粉丝'  #get uid
        ffan_nums = re.findall(re.compile(fan_nums), funs)

        uurl = ixpath.attrib['href']
        #print uurl

        uid = r'http://www.douguo.com/u/u(\d*).html'  #get uid
        fuid = re.findall(re.compile(uid), ixpath.attrib['href'])
        #print fuid

        hot_rank = i.xpath('./span')[0].text
        if hot_rank == None:
            hot_rank = 0
        else:
            hot_rank = int(hot_rank)

        print int(fuid[0]), name, uurl, '1', int(ffan_nums[0]), hot_rank, now, now

        #print span.text
        # conn = MySQLdb.connect(
        # host = '127.0.0.1',
        # port = 3306,
        # user = 'root',
        # passwd = 'root',
        # db = 'douguo',
        # charset="utf8"
        # )
        # cur = conn.cursor()
        # sqli = 'insert into topuser (uid,name,uurl,status,fan_nums,hot_rank,created_time,updated_time) values (%s,%s,%s,%s,%s,%s,%s,%s)'
        # cur.execute(sqli,(int(fuid[0]),name,uurl,'1',int(ffan_nums[0]),hot_rank,now,now))
        # conn.commit()
        # cur.close()


        # INSERT INTO topuser
        # (uid,NAME,uurl,STATUS,fan_nums,hot_rank,created_time,updated_time)
        # VALUES
        # (40064469316319,'姜叔的日食记','http://www.douguo.com/u/u40064469316319.html',1,14277,0,'2016-02-22 15:08:10.066000','2016-02-22 15:08:10.066000')