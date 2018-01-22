# -*- coding: utf-8 -*-

# a = 1
# b = 3
# print a.__add__(b)
# print a


# class Int:
# ctype = "Class::Int"
# def __init__(self, val):
#         self._val = val
#     def __getattribute__(self, name):
#         print("@_@ doesn't want to give `{}' to you!".format(name))
#         return "@_@"
#
# a = Int(2)
# print a.ctype


# class Int:
#     ctype = "Class::Int"
#     def __init__(self, val):
#         self._val = val
#     def __getattribute__(self, name):
#         print("👿 doesn't want to give `{}' to you!".format(name))
#         return "🐍"
# a = Int(2)
# print(a.ctype)


# class Str:
#     def __init__(self, val):
#         self._val = val
#     def __get__(self, name, ctype=None):
#         print("You can __get__ anything from here!")
#         return self._val
# class Int:
#     ctype = Str("Class::Int")
#     def __init__(self, val):
#         self._val = val
#     def __getattribute__(self, name):
#         return type(self).__dict__[name].__get__(None, type(self))
# a = Int(2)
# print(a.ctype)


# class Int:
#     def __init__(self, val):
#         self._val = val
#         self._ctype = None
#
#     def get_ctype(self):
#         print("INFO: You can get `ctype`")
#         return self._ctype
#     def set_ctype(self, val):
#         print("INFO: You're setting `ctype` =", val)
#         self._ctype=val
#     ctype = property(fget=get_ctype, fset=set_ctype, doc="Property `ctype`")
#
# a = Int(4)
# print(a.ctype)
# a.ctype = "Class::Int"
# print(a.ctype)