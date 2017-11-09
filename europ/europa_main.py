#coding=utf8
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

import urllib
from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time,datetime,os,selenium
import logging;
import logging.config;
logging.basicConfig()
import multiprocessing


def write_txt(file_name=None,txt=None):
    file_name = file_name + '.txt'
    wf = open(file_name,'a+')
    wf.write(txt+'\n')
    wf.close()


def select_ok(j,part_name,dir):
    try:
        print u"点击第"+str(j+1)+u"行"
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='categoriesDiv']/ul/li[1]/a/ins")))
        if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[j].get_attribute("class") == u'unchecked':
            browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[j].click()
        time.sleep(1)
    except Exception,err:
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"时间选择错误发生行数:"+ str(j+1)
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"时间选择错误发生行数:"+ str(j+1))
    # if browser.find_elements_by_xpath(".//*[@id='categoriesDiv']/ul/li/a/ins")[j].is_selected() == False:
    #     select_ok(j)

def download(j = None,time_tag= None,type = '',dir = None,try_num = 0,part_name = None):
    # write_txt(dir+u"/"+part_name+".log","ok")
    # j = 10
    # if try_num != 0:
    #     try_num = 0
    try:
        # ui.WebDriverWait(browser, 5, 0.5).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='downloadDialog']")))
        # print "downloadDialog exist"
        ui.WebDriverWait(browser, 600, 1).until_not(EC.visibility_of_element_located((By.XPATH,".//*[@id='downloadDialog']")))
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j+1))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j+1)
        # time.sleep(5)
        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[0])
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='changeSelectionFormMock']/a[1]")))
        browser.find_element_by_xpath('''.//*[@id='changeSelectionFormMock']/a[1]''').click()
        time.sleep(5)
        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[1])
        time.sleep(5)
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='tabs']/div/a")))
        browser.find_elements_by_xpath('''.//*[@id='tabs']/div/a''')[time_tag].click()
        time.sleep(10)
        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[1])
        if type == 'year':
            ui.WebDriverWait(browser, 300, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[contains(@id,'ck_')]")))
            browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
            browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
            # browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]''')[j].click()
            browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]''')[j].click()
        elif type == 'month' and j > 0:
            # ui.WebDriverWait(browser, 300, 1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='categoriesDiv']/ul/li/a")))
            time.sleep(3)
            select_ok(j,part_name,dir)

            browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[j-1].click()
            time.sleep(1)
            if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a''')[0].get_attribute("class") == u'checked':
                browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
            time.sleep(5)
            # browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[j-1].send_keys(Keys.SPACE)
        browser.find_element_by_xpath('''.//*[@id='updateExtractionButton']''').click()

        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[0])
        ui.WebDriverWait(browser, 30, 1).until_not(EC.element_to_be_clickable((By.XPATH,".//*[@id='body']/div[8]")))

        # time.sleep(3)
        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[0])
        ui.WebDriverWait(browser, 30, 1).until_not(EC.element_to_be_clickable((By.XPATH,".//*[@id='body']/div[7]")))

        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[0])
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='EXCEL']/ol/li[10]/input")))
        browser.find_element_by_xpath('''.//*[@id='excelFULL_EXTRACTION_SEPARATE_SHEET']''').click()
        browser.find_element_by_xpath('''.//*[@id='EXCEL']/ol/li[10]/input''').click()
        time.sleep(10)
        # print str(j+1)+u",请求下载数据"
        # ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='EXCEL']/ol/li[10]/input")))
        # browser.find_element_by_xpath('''.//*[@id='changeSelectionFormMock']/a[2]''').click()
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"请求下载数据:"+ str(j+1))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"请求下载数据:"+ str(j+1)

    except Exception,err:
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"下载错误行数:"+ str(j+1)+ u":重试次数:"+ str(try_num))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"下载错误行数:"+ str(j+1)+ u":重试次数:"+ str(try_num)

        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"错误信息:"+ str(err))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"错误信息:"+ str(err)
        try_num = try_num + 1

        if try_num < 3:
            all_handles=browser.window_handles
            if len(all_handles) > 1:
                browser.switch_to_window(all_handles[1])
                browser.close()
            all_handles=browser.window_handles
            browser.switch_to_window(all_handles[0])
            download(j ,time_tag,type ,dir ,try_num,part_name)
        else:
            return False
    # ui.WebDriverWait(browser, 180, 1).until_not(EC.visibility_of_element_located((By.XPATH,".//*[@id='downloadDialog']")))
    # write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j-1))
    # print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j+1)

def login_europa(part_name = None,dir = None):
    # write_txt(dir+u"/"+part_name+".log","ok")
    # login_url = "http://ec.europa.eu/eurostat/data/database"
    j = 0
    try:
        if part_name == None:
            return

        login_url = "http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset="+part_name+"&lang=en"
        # http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=ert_bil_eur_m&lang=en
        print login_url
        browser.get(login_url)
        time.sleep(10)

        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='TIME']/button")))
        browser.find_element_by_xpath('''.//*[@id='TIME']/button''').click()
        time.sleep(5)

        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[1])
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='tabs']/div/a")))
        tabs = browser.find_elements_by_xpath('''.//*[@id='tabs']/div/a''')
        stop_len = 1
        time_tag = 0
        type = ''
        for i in range(0,len(tabs)):
            all_handles=browser.window_handles
            browser.switch_to_window(all_handles[1])
            browser.find_elements_by_xpath('''.//*[@id='tabs']/div/a''')[i].click()
            # time.sleep(1)
            tab_name =  browser.find_elements_by_xpath('''.//*[@id='tabs']/div/a''')[i].text

            if tab_name != u"TIME":
                browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
                time.sleep(1)
                write_txt(dir+u"/"+part_name+".log",tab_name+"_len:"+str(len(browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]''')))+",size:"+str(browser.find_element_by_xpath('''.//*[@id='extractionCounter']''').text))
                print tab_name+"_len:"+str(len(browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]''')))+",size:"+str(browser.find_element_by_xpath('''.//*[@id='extractionCounter']''').text)

            elif tab_name == u"TIME":
                # .//*[contains(@id,'ck_')]  年/季
                # .//*[@id='categoriesDiv']/ul/li/ul/li/a/ins 月
                # .//*[@id='categoriesDiv']/ul/li/ul/li/ul/li/a/ins 日
                if len(browser.find_elements_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''')) > 0:
                    type = 'year'
                    browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
                    browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
                    browser.find_element_by_xpath('''.//*[contains(@id,'ck_')]''').click()
                    stop_len = len(browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]'''))
                    time_tag = i

                elif len(browser.find_elements_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''')) ==  0 and len(browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/ul/li/a/ins''')) > 0:
                    type = 'month'
                    ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='categoriesDiv']/ul/li[1]/a/ins")))
                    time.sleep(1)
                    if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].get_attribute("class") == u'unchecked':
                        browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].click()
                    time.sleep(1)
                    browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
                    time.sleep(3)

                    if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a''')[0].get_attribute("class") == u'unchecked':
                        browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
                    if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a''')[1].get_attribute("class") == u'checked':
                        browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].click()
                    time.sleep(1)
                    stop_len = len(browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins'''))
                    time_tag = i

                elif len(browser.find_elements_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''')) ==  0 and len(browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/ul/li/a/ins''')) == 0:
                    type = 'month'
                    ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='categoriesDiv']/ul/li[1]/a/ins")))
                    time.sleep(1)
                    if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].get_attribute("class") == u'unchecked':
                        browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].click()
                    time.sleep(1)
                    # browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
                    time.sleep(3)

                    if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a''')[0].get_attribute("class") == u'unchecked':
                        browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
                    if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a''')[1].get_attribute("class") == u'checked':
                        browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].click()
                    time.sleep(1)
                    stop_len = len(browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins'''))
                    time_tag = i


        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"条件总数:"+ str(stop_len)
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"条件总数:"+ str(stop_len))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"标签页次序:"+ str(time_tag)
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"标签页次序:"+ str(time_tag))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"类型:"+ type
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"类型:"+ type)


        browser.find_element_by_xpath('''.//*[@id='updateExtractionButton']''').click()

        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[0])
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='nav']/ul/li[3]/a")))
        browser.find_element_by_xpath('''.//*[@id='nav']/ul/li[3]/a''').click()

        # ui.WebDriverWait(browser, 30, 1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='EXCEL']/ol/li[10]/input")))
        # browser.find_element_by_xpath('''.//*[@id='EXCEL']/ol/li[10]/input''').click()

        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[0])



        for j in range(0,stop_len):
            is_go_on = download(j ,time_tag,type,dir,0,part_name)
            if is_go_on == False:
                break

        ui.WebDriverWait(browser, 600, 1).until_not(EC.visibility_of_element_located((By.XPATH,".//*[@id='downloadDialog']")))
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j+1))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j+1)

        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"完成下载")
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"完成下载"

        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name + u":关闭浏览器")
        browser.quit()
    except Exception,Error:
        print Error
        browser.quit()
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name + u":轮询错误,关闭浏览器,行数:"+ str(j+1)
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name + u":轮询错误,关闭浏览器,行数:"+ str(j+1))





def do_work(part_name = None,dir = None):
    if part_name == None:
        return
    fp = webdriver.FirefoxProfile("C:\Users\yaoxiang.sun\AppData\Roaming\Mozilla\Firefox\Profiles\ooe225oa.default")
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir", dir)

    proxyIp = "112.74.28.173"
    proxyPort = "1080"
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http", proxyIp)
    fp.set_preference("network.proxy.http_port", proxyPort)

    # print os.getcwd()
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
    global browser
    browser = webdriver.Firefox(firefox_profile=fp)
    #登录
    write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name + u":启动浏览器")
    login_europa(part_name,dir)




def file_work(part_name = None):
    # part_name = 'irt_lt_mcby_m'
    # 112.74.28.173	1080
    # global dir
    dir = os.getcwd()+"\\download\\"+part_name

    if os.path.exists(dir) == False:
        os.mkdir(dir)
    write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":" +part_name+":启动下载脚本")
    do_work(part_name,dir)

if __name__ == '__main__':
    part_name_list = [
        "irt_lt_mcby_m",
        "irt_lt_gby10_m",
        "irt_st_q",
        "irt_st_m",
        "prc_hicp_midx",
        "prc_hicp_manr",
        "prc_hicp_mmor",
        "prc_hicp_mv12r",
        "prc_hicp_aind",
        "prc_hicp_cow",
        "prc_hicp_inw",
        "prc_hicp_fp",
        "prc_hicp_cind",
        "prc_hicp_cann",
        # "prc_hicp_cmon",
    ]
    #
    for part_name in part_name_list:
        file_work(part_name)
    # file_work('prc_hicp_cmon')
    # multiprocessing.freeze_support()
    # europ_pool = multiprocessing.Pool(processes= 2)

    part_name_list2 = [
                    "sts_inpp_m",
                    "ext_st_eu28sitc",
                    "ext_st_ea19sitc",
                    "ext_st_eu28bec",
                    "ext_st_ea19bec",
                    "gov_10dd_edpt1",
                    "gov_10q_ggdebt",
                    ]

    for part_name in part_name_list2:
        file_work(part_name)