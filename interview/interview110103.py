# -*- coding: utf-8 -*-

# from contextlib import contextmanager as cm
# _G = {"counter": 99, "user": "admin"}
#
# @cm
# def ref():
# counter = _G["counter"]
#     yield _G
#     _G["counter"] = counter
#
# with ref() as r1, ref() as r2:
#     for _ in range(3):
#         r1["counter"] -= 1
#         print("COUNTER #ref1: {}".format(_G["counter"]))
#         r2["counter"] += 2
#         print("COUNTER #ref2: {}".format(_G["counter"]))
# print("*"*20)
# print(_G)

from random import randrange

# tup = (randrange(-100,100) for _ in range(10))
# print sorted(tup)
# for i in tup:
#     print i
# print sorted(tup)
# tup = (randrange(-100,100) for _ in range(10))
# print sorted(tup,key = abs)
#
lst = list(zip("hello world i am who".split(), [randrange(1, 10) for _ in range(5)]))
# print lst
# print sorted(lst ,key = lambda item : item[0])


from operator import itemgetter, attrgetter

# print(lst)
# print(sorted(lst, key=itemgetter(1)))

# 一切都只是函数
fitemgetter = lambda ind: lambda item: item[ind]
# print(sorted(lst, key=fitemgetter(1)))

class P(object):
    def __init__(self, w, n):
        self.w = w
        self.n = n

    def __repr__(self):
        return "{}=>{}".format(self.w, self.n)


ps = [P(i[0], i[1]) for i in lst]

print(sorted(ps, key=attrgetter('n'), reverse=True))
print(sorted(ps, key=attrgetter('n'), reverse=False))