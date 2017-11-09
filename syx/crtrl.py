#!/usr/bin/env Python
import sys
import time

from syx import ostry


while True:
    time.sleep(4)
    try:
        ret = ostry.popen('ps -C apache -o pid,cmd').readlines()
        if len(ret) < 2:
            print "apache 进程异常退出， 4 秒后重新启动"
        time.sleep(3)
        ostry.system("service apache2 restart")
    except:
        print "Error", sys.exc_info()[1]
