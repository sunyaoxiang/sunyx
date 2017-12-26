# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import logging
from lxml import etree as Etree
import os


def do_post_body(url, data="", headers=None):
    if headers == None:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
        }
    try:
        req = urllib2.Request(url, data=data, headers=headers)
        f = urllib2.urlopen(req, timeout=60)
        if f.getcode() == 200:
            logging.getLogger().info("Request sucess ...")
            return f.read()
        else:
            logging.getLogger().info('http err code not 200', url)
    except Exception, e:
        logging.getLogger().info("failed request %s", url)
        logging.getLogger().error(e)


def saveHtml(file_name, file_content):
    with open(file_name.replace('/', '_').replace(":", "=").replace("<", "(").replace(">", ")") + ".html", "wb") as f:
        f.write(file_content)


def get_index_info():
    url = "http://www.yiibai.com/"

    dir = "\\" + u"首页"
    if os.path.exists(os.getcwd() + dir) == False:
        os.mkdir(os.getcwd() + dir)
    file_name = u".\首页\index"

    response = do_post_body(url)
    saveHtml(file_name, response)
    htmlSource = Etree.HTML(response)
    seconde_url = htmlSource.xpath('''.//*[@id='navs']/article/div/div/ul/li/a''')

    seconde_url_list = []
    for seconde_i in seconde_url:
        seconde_url_list.append({
            "url": str(seconde_i.attrib['href']),
            "name": seconde_i.text
        })

    return seconde_url_list


def get_total_view(url_list):
    if url_list == None:
        return
    for dat in url_list[24:]:
        total_url = dat['url']
        name = dat['name']
        dir = "\\" + name
        if os.path.exists(os.getcwd() + dir) == False:
            os.mkdir(os.getcwd() + dir)

        file_name = "." + dir + "\\" + name

        total_response = do_post_body(total_url)
        saveHtml(file_name, total_response)
        total_htmlSource = Etree.HTML(total_response)

        detail_url = total_htmlSource.xpath('''.//*[@class='container container-page']/div/div/ul/li/a''')

        detail_url_list = []
        try:
            for detail_i in detail_url[1:]:
                detail_url_list.append({
                    "url": str(detail_i.attrib['href']),
                    "name": detail_i.text,
                    "dir": dir
                })
        except:
            pass

        get_detail_view(detail_url_list)


def get_detail_view(url_list):
    if url_list == None:
        return
    for dat in url_list:
        detail_url = dat['url']
        name = dat['name']
        dir = dat['dir']
        file_name = "." + dir + "\\" + name

        total_response = do_post_body(detail_url)
        saveHtml(file_name, total_response)


if __name__ == '__main__':
    seconde_url_list = get_index_info()

    get_total_view(seconde_url_list)