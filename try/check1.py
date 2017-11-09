#coding=utf8

from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler(daemon=False);

@scheduler.scheduled_job(trigger="interval", seconds = 1, max_instances=1)
def api_rule_I(isauto = None):
    print 'error'

scheduler.start()
print 'end'