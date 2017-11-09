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


def select_ok(j):
    try:
        write_txt(dir+u"/"+part_name+".log","ok")
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='categoriesDiv']/ul/li[1]/a/ins")))
        browser.find_element_by_xpath('''.//*[@id='categoriesDiv']/ul/li[1]/a/ins''').click()
        time.sleep(1)
    except Exception,err:
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"时间选择错误发生行数:"+ str(j)
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"时间选择错误发生行数:"+ str(j))
    # if browser.find_elements_by_xpath(".//*[@id='categoriesDiv']/ul/li/a/ins")[j].is_selected() == False:
    #     select_ok(j)

def download(j = None,time_tag= None,type = '',dir = None,try_num = 0):
    # write_txt(dir+u"/"+part_name+".log","ok")
    # j = 10
    # if try_num != 0:
    #     try_num = 0
    try:
        # ui.WebDriverWait(browser, 5, 0.5).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='downloadDialog']")))
        # print "downloadDialog exist"
        ui.WebDriverWait(browser, 300, 1).until_not(EC.visibility_of_element_located((By.XPATH,".//*[@id='downloadDialog']")))
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j-1))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"文件加载完成，开始下载:"+ str(j)
        # time.sleep(5)
        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[0])
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='changeSelectionFormMock']/a[1]")))
        browser.find_element_by_xpath('''.//*[@id='changeSelectionFormMock']/a[1]''').click()
        # time.sleep(1)
        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[1])
        # time.sleep(1)
        ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='tabs']/div/a")))
        browser.find_elements_by_xpath('''.//*[@id='tabs']/div/a''')[time_tag].click()

        all_handles=browser.window_handles
        browser.switch_to_window(all_handles[1])
        if type == 'year':
            ui.WebDriverWait(browser, 300, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[contains(@id,'ck_')]")))
            browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
            browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
            # browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]''')[j].click()
            browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]''')[j].click()
        elif type == 'month' and j > 0:
            time.sleep(1)
            select_ok(j)

            browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[j-1].click()
            if browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].is_selected() == True:
                browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
            time.sleep(1)
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
        # time.sleep(5)
        # print str(j)+u",请求下载数据"
        # ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='EXCEL']/ol/li[10]/input")))
        # browser.find_element_by_xpath('''.//*[@id='changeSelectionFormMock']/a[2]''').click()
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"请求下载数据:"+ str(j))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"请求下载数据:"+ str(j)

    except Exception,err:
        write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"下载错误行数:"+ str(j)+ u":重试次数:"+ str(try_num))
        print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"请求下载数据:"+ str(j)

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
            download(j,time_tag,type)
        else:
            return False


def login_europa(part_name = None,dir = None):
    # write_txt(dir+u"/"+part_name+".log","ok")
    # login_url = "http://ec.europa.eu/eurostat/data/database"
    if part_name == None:
        return

    login_url = "http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset="+part_name+"&lang=en"
    # http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=ert_bil_eur_m&lang=en
    print login_url
    browser.get(login_url)
    time.sleep(2)

    browser.find_element_by_xpath('''.//*[@id='TIME']/button''').click()
    time.sleep(1)

    all_handles=browser.window_handles
    browser.switch_to_window(all_handles[1])
    ui.WebDriverWait(browser, 30, 1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='tabs']/div/a")))
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
            print tab_name+"_len:"+str(len(browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]''')))+",size:"+str(browser.find_element_by_xpath('''.//*[@id='extractionCounter']''').text)

        elif tab_name == u"TIME":
            # .//*[contains(@id,'ck_')]  年/季
            # .//*[@id='categoriesDiv']/ul/li/ul/li/a/ins 月
            # .//*[@id='categoriesDiv']/ul/li/ul/li/ul/li/a/ins 日
            if len(browser.find_elements_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''')) > 0:
                browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
                browser.find_element_by_xpath('''.//*[@id='checkUncheckAllCheckboxTable']''').click()
                browser.find_element_by_xpath('''.//*[contains(@id,'ck_')]''').click()
                stop_len = len(browser.find_elements_by_xpath('''.//*[contains(@id,'ck_')]'''))
                time_tag = i
                type = 'year'

            elif len(browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')) > 0:
                ui.WebDriverWait(browser, 30, 1).until(EC.element_to_be_clickable((By.XPATH,".//*[@id='categoriesDiv']/ul/li[1]/a/ins")))
                time.sleep(1)
                browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].click()
                time.sleep(1)
                browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
                time.sleep(1)
                browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[0].click()
                time.sleep(1)
                browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins''')[1].click()
                time.sleep(1)
                stop_len = len(browser.find_elements_by_xpath('''.//*[@id='categoriesDiv']/ul/li/a/ins'''))
                time_tag = i
                type = 'month'

    print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"条件总数:"+ str(stop_len)
    write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"条件总数:"+ str(stop_len))
    print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"标签页次序:"+ str(time_tag)
    write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"标签页次序:"+ str(time_tag))
    print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"类型:"+ type
    write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"类型:"+ type)


    browser.find_element_by_xpath('''.//*[@id='updateExtractionButton']''').click()

    all_handles=browser.window_handles
    browser.switch_to_window(all_handles[0])
    browser.find_element_by_xpath('''.//*[@id='nav']/ul/li[3]/a''').click()

    # ui.WebDriverWait(browser, 30, 1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='EXCEL']/ol/li[10]/input")))
    # browser.find_element_by_xpath('''.//*[@id='EXCEL']/ol/li[10]/input''').click()

    all_handles=browser.window_handles
    browser.switch_to_window(all_handles[0])

    for j in range(0,stop_len):
        is_go_on = download(j,time_tag,type,dir)
        if is_go_on == False:
            break

    write_txt(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"完成下载")
    print str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name +":"+u"完成下载"

    write_txt(dir+u"/"+part_name+".log",str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ":"+part_name + u":关闭浏览器")
    browser.quit()


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
        # "ert_bil_eur_a",
        # "ert_bil_eur_q",
        # "ert_bil_eur_m",
        # "ert_eff_ic_m",
        # "irt_euryld_m",
        "irt_euryld_d",
        # "irt_lt_mcby_a",
        # "irt_lt_mcby_q",
        "irt_lt_mcby_m",
        "irt_lt_mcby_d",
        "irt_lt_gby10_a",
        "irt_lt_gby10_m",
        "irt_st_a",
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
        "prc_hicp_caon",
        "prc_hpi_a",
        "prc_hpi_q",
        "prc_hpi_inw",
        "prc_hpi_hs",
        "prc_hpi_ooa",
        "prc_hpi_ooq",
        "prc_hpi_ooinw",
    ]

    for part_name in part_name_list:
        file_work(part_name)

    # multiprocessing.freeze_support()
    # europ_pool = multiprocessing.Pool(processes= 2)
    # for part_name in part_name_list:
    #     europ_pool.apply_async(file_work,args = (part_name,))
    #     #
    # europ_pool.close()
    # europ_pool.join()
