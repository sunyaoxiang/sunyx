# -*- coding: utf-8 -*-
from time import time as _time
from datetime import *

# d1 = date(2016, 3, 29)
# d2 = date.today()
# d3 = date.fromtimestamp(_time())
#
# print(d1)
# print(d2)
# print(d3)


# t1 = time(22, 57, 6, 6)
# t2 = datetime.now().time()
# print(t1)
# print(t2)


# dt1 = datetime(2016, 3, 30, 22, 2)
# dt2 = datetime.now()
# dt3 = datetime.fromtimestamp(_time())
# print(dt1)
# print(dt2)
# print(dt3)

# dt = datetime.now()
# dt = datetime.fromtimestamp(_time())
#
# d = dt.date()
# t = dt.time()
#
# print("Date: {}\nTime: {}".format(d, t))
#
# print("Datetime: {}".format(datetime.combine(date.today(), time(2,3,3))))


# td = timedelta(weeks=1, days=2, hours=3,minutes=4, seconds=0, microseconds=0, milliseconds=0)
#
# print("Time duration: {}".format(td))


# current = datetime.now()
# today = datetime.combine(date.today(), time(0,0,0))
#
# td = current - today
# print("{:.0f}s of Today".format(td.total_seconds()))
#
# today = date.today()
# lastyear = today.replace(year=today.year-1)
# print(today - lastyear)
#
# t1 = current.time()
# t2 = time(0, 0, 0)
# try:
# print(t1 - t2)
# except TypeError as err:
# print(err)


fmat = "%y/%m/%d"
dt = datetime.now()
dt = dt - timedelta(days=22)

print(dt.strftime(fmat))

# 当然也可以用
print("{}/{}/{}".format(dt.strftime("%y"), dt.month, dt.day))