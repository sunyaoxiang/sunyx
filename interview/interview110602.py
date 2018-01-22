# -*- coding: utf-8 -*-

# def jump_range(upper):
# index = 0
# while index < upper:
#         jump = yield index
#         if jump is None:
#             jump = 1
#         index += jump*2
# jump = jump_range(100)
# # print(jump)
# print(jump.send(None))
# print(jump.send(2))
# print(jump.send(2))
# print(jump.send(None))
# print(jump.send(None))
# print(jump.send(None))


# def MyGenerator():
#     list = range(10)
#     for i in list:
#         yield i
#         # print i
#
#
# gen = MyGenerator()
# print gen.next()
# print gen.next()
# print gen.next()
# print gen.next()
# print gen.next()
# print gen.next()
# print gen.next()
# print gen.next()
# print gen.next()
# print gen.next()


# def wait_index(i):
#     # processing i...
#     return (yield i)
#
# def jump_range(upper):
#     index = 0
#     while index < upper:
#         jump = yield from wait_index(index)
#         if jump is None:
#             jump = 1
#         index += jump
# jump = jump_range(5)
# print(jump)
# print(jump.send(None))
# print(jump.send(3))
# print(jump.send(None))


# import asyncio
# import time
# import types
#
# @types.coroutine
# def _sum(x, y):
#     print("Compute {} + {}...".format(x, y))
#     yield time.sleep(2.0)
#     return x+y
# @types.coroutine
# def compute_sum(x, y):
#     result = yield from _sum(x, y)
#     print("{} + {} = {}".format(x, y, result))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(compute_sum(0,0))