# coding=utf-8
import urllib, urllib2

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://xxx.xxx.x.x:8080'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)