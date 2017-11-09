#coding=utf-8
import urllib,urllib2,re
import lxml
urllist = []
url = 'http://www.douguo.com/top/remenyonghu/'
urllist.append(url)
for i in [30,60,90]:
    url = 'http://www.douguo.com/top/remenyonghu/'
    url = url + '/'+str(i)
    #print url
    urllist.append(url)

for u in urllist:
    request = urllib2.Request(u)
    request.add_header('Cache-Control', 'max-age=0')
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0')
    request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    request.add_header('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    response = urllib2.urlopen(request).read()
    #print response
    uurl = r'<a href="(http://www.douguo.com/u/u\d*.html)" target='#get uurl
    fuurl = re.findall(re.compile(uurl),response)

    uid = r'http://www.douguo.com/u/u(\d*).html'#get uid
    fuid = re.findall(re.compile(uid),response)

    #name = ur'<a title="[\u4e00-\u9fa5]*" target="_blank"'#get uid
    #fname = re.findall(re.compile(name),response.decode('utf8'))
    #print fname

    fan_nums = r'<div class="favnum">(\d*)粉丝</div>'#get uid
    ffan_nums = re.findall(re.compile(fan_nums),response)

    #hot_rank = r'(\d*)</span>/n<a title='#get uid
    #fhot_rank = re.findall(re.compile(hot_rank),response)
    #print len(fuurl),len(fuid),len(fname),len(ffan_nums)
    for i in range(len(fuurl)):
        print fuurl[i],fuid[i],ffan_nums[i]