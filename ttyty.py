# -*- coding: utf-8 -*-
import datetime


from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler(daemon=False)



@scheduler.scheduled_job(trigger="cron",minute = "41,42-43",second = "*/2")
def check_report_meta():
    print str(datetime.datetime.now())


if __name__ == '__main__':
    # check_report_meta()
    scheduler.start()