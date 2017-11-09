# -*- coding: utf-8 -*-

# from __future__ import division
#
# print 8//7
# print 8/7


# from itertools import cycle, count, repeat
# # print(count.__doc__)
#
# counter = count()
# print(next(counter))
# print(next(counter))
# # print(list(map(lambda x, y: x+y, range(10), counter)))
#
# odd_counter = map(lambda x: 'Odd#{}'.format(x), count(1, 2))
# print(next(odd_counter))
# print(next(odd_counter))


from enum import Enum, IntEnum, unique

# try:
#     @unique
#     class WEEKDAY(Enum):
#         MON = 1
#         TUS = 2
#         WEN = 3
#         THU = 4
#         FRI = 5
# except ValueError as e:
#     print(e)
#
# try:
#     class Color(IntEnum):
#         RED   = 0
#         GREEN = 1
#         BLUE  = 2
# except ValueError as e:
#     print(e)

class Color(Enum):
    R = 0
    G = 1
    B = 2

# try:
#     Color.R = 2
# except AttributeError as e:
#     print(e)

red = Color(0)
green = Color(1)
blue = Color(2)
# print(red, green, blue)
# print(red is Color.R)
# print(red == Color.R)
# print(red is blue)
# print(green != Color.B)
# print(red == 0)

print(red.B)
print(red.B.G.R)