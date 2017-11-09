# -*- coding: utf-8 -*-
import os
from selenium import webdriver


service_args = []
# 忽略SSL错误
service_args.append('--ignore-ssl-errors=yes')
# 不下载图片
service_args.append('--load-images=no')
# 使用硬盘缓存
service_args.append('--disk-cache=true')
# 指定Cookie文件
# if cookie_file:
service_args.append('--cookies-file=%s' % "--cookies-file=c:\\users\\yaoxiang.sun\\appdata\\local\\temp\\tmp")
try:
    browser = webdriver.PhantomJS(service_args=service_args)
except Exception, e:
   print e

url = "http://index.baidu.com/"
browser.get(url)
# cookie_list = driver.get_cookies()
browser.find_element_by_xpath('''//*[@id="userbar"]/ul/li[4]/a''').click()
browser.find_element_by_xpath('''//*[@id="TANGRAM_12__userName"]''').send_keys(ur"**")
browser.find_element_by_xpath('''//*[@id="TANGRAM_12__password"]''').send_keys(ur"")
browser.find_element_by_xpath('''//*[@id="TANGRAM_12__submit"]''').click()

browser.get_screenshot_as_file("login.png")
print "ok"