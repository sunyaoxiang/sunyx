# coding=utf-8
import urllib


url = 'http://www.cnblogs.com/fnng/p/3565912.html'
f = urllib.urlopen(url).getcode()

print f