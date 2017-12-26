# coding=utf8
import sys;

reload(sys);
sys.setdefaultencoding("utf8")
import time
import datetime
import logging;
import logging.config;

logging.basicConfig()

from new2 import deal_rule

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(daemon=False);


@scheduler.scheduled_job(trigger="interval", seconds=1, max_instances=1)
def new1(isauto=None):
    t1 = datetime.datetime.now()
    print "new1:", t1
    deal_rule(t1)


scheduler.start();