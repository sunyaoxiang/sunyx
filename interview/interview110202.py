# -*- coding: utf-8 -*-


from calendar import TextCalendar, HTMLCalendar

tc = TextCalendar(firstweekday=6)
# print [tc.prmonth(x,y) for x in range(2010,2011) for y in range(1,13)]

for x in range(2010,2011):
    for y in range(1,13):
        tc.prmonth(x,y)


# f = lambda x : x +10
# print map(f,range(10))

# f = lambda x,y : x * y
# list = []
# list.append(f)
# print list
# print list[0](range(10),2)
# # print reduce(f,range(1,10))


# f = lambda x : x < 5
# print filter(f,range(10))
# lambda x+y : x,y for x,y in (range(2016,2017) ,range(1,13))


# class test():
#     def __init__(self,name = "self name"):
#         self.name = name
#     def printname(self,name = "self name"):
#         if name is None:
#             name = self.name
#         print name
#
# lista = []
# printn = test().printname
# lista.append(printn)
#
# lista[0]()
# lista[0]("list name")