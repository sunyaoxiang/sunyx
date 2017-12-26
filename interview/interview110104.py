# -*- coding: utf-8 -*-

# def do_func_n(func):
# print "start action func:"
#     print func()
#     print "action func end"
#
# def addn(num = 0):
#     num += 1
#     return num
#
# do_func_n(addn)

#
# def do_func_n(func):
#     print "start action func:"
#     print func
#     print "action func end"
#
# def addn(num = 0):
#     num += 1
#     return num
#
# do_func_n(addn())


# def do_func_n(func):
#     def funx():
#         print "start action func:"
#         print func()
#         print "action func end"
#     return funx
#
# @do_func_n
# def addn(num = 0):
#     num += 1
#     return num
#
# addn()


# from time import sleep, time
# def timer(Cls):
#     def wraper():
#         s = time()
#         obj = Cls()
#         e = time()
#         print("Cost {:.3f}s to init.".format(e - s))
#         return obj
#     return wraper
#
# @timer
# class Obj:
#     def __init__(self):
#         print("Hello")
#         sleep(3)
#         print("Obj")
#
# o = Obj()


# class HTML(object):
#     """
#         Baking HTML Tags!
#     """
#     def __init__(self, tag="p", title = 't'):
#         print("LOG: Baking Tag <{}> title {}!".format(tag,title))
#         self.tag = tag
#         # pass
#     def __call__(self, func):
#         print "do action"
#         return lambda: "<{0}>{1}</{0}>".format(self.tag, func(), self.tag)
#
# @HTML("html","past")
# @HTML("body")
# @HTML("div")
# def body():
#     return "Hello"
#
# print(body())


# RULES = {}
# def route(rule):
#     def decorator(hand):
#         RULES.update({rule: hand})
#         return hand
#     return decorator
#
# @route("/")
# def index():
#     print("Hello world!")
#
# def home():
#     print("Welcome Home!")
#
# home = route("/home")(home)

# index()
# home()
# print(RULES)
# @route("/login")
# def login(user = "user", pwd = "pwd"):
#     print("DB.findOne({{{}, {}}})".format(user, pwd))
# login("hail", "python")


# def log(f):
#     def wraper(*args, **kargs):
#         print("INFO: Start Logging")
#         f(*args, **kargs)
#         print("INFO: Finish Logging")
#     return wraper
#
# @log
# def run(hello = "world"):
#     print("Hello {}".format(hello))
# run("Python")


# from functools import update_wrapper
#
# class HTML(object):
#     def __init__(self, tag="p"):
#         print("LOG: Baking Tag <{}>!".format(tag))
#         self.tag = tag
#     def __call__(self, func):
#         wraper = lambda: "<{0}>{1}</{0}>".format(self.tag, func(), self.tag)
#         update_wrapper(wraper, func)
#         return wraper
#
# @HTML("body")
# def body():
#     return "Hello, body!"
#
# print(body.__name__)
# print(body.__doc__)


from functools import update_wrapper, partial


def my_wraps(wrapped):
    return partial(update_wrapper, wrapped=wrapped)


def log(func):
    @my_wraps(func)
    def wraper():
        print("INFO: Starting {}".format(func.__name__))
        func()
        print("INFO: Finishing {}".format(func.__name__))

    return wraper


@log
def run():
    """
    Docs' of run
    """
    print("Running run...")


print(run.__name__)
print(run.__doc__)