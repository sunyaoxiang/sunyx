# coding=utf8
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
import time
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(daemon=False);


@scheduler.scheduled_job(trigger="interval", seconds=1, max_instances=1)
def new1(isauto=None):
    t1 = datetime.datetime.now()
    print "new2:", t1
    deal_rule(t1)


def deal_rule(t=None):
    time.sleep(3)
    t2 = datetime.datetime.now()
    print "deal_rule:", t2
