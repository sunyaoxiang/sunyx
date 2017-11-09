# coding=utf-8
import datetime, calendar


year = int(datetime.datetime.today().strftime("%Y"))
now_month = int(datetime.datetime.today().strftime("%m"))
# now_month = 12
if now_month == 1:
    last_month = 12;
    year = year - 1
else:
    last_month = now_month -1;

print year,last_month
print calendar.monthrange(year,last_month)[1]

last_month_first_day = datetime.datetime.strptime((str(year)+"-"+str(last_month)+"-"+str(calendar.monthrange(year,last_month)[0])),'%Y-%m-%d').strftime("%Y-%m-%d")

last_month_last_day = datetime.datetime.strptime((str(year)+"-"+str(last_month)+"-"+str(calendar.monthrange(year,last_month)[1])),'%Y-%m-%d').strftime("%Y-%m-%d")
print last_month_first_day,last_month_last_day


lastSUNDAY = datetime.date.today()
oneday = datetime.timedelta(days = 1)
while lastSUNDAY.weekday() != calendar.SUNDAY:
    lastSUNDAY -= oneday
lastSUNDAY =  lastSUNDAY.strftime("%Y-%m-%d")
print lastSUNDAY


lastMONDAY = datetime.date.today()
oneday = datetime.timedelta(days = 1)
while lastMONDAY.weekday() != calendar.MONDAY:
    lastMONDAY -= oneday
lastMONDAY = lastMONDAY - datetime.timedelta(days = 7)
lastMONDAY =  lastMONDAY.strftime("%Y-%m-%d")
print lastMONDAY

# bash -x restart.sh dp05_monitor.py

print datetime.datetime.now().weekday()