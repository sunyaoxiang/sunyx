# coding=utf-8

class A(object):
    x = 1


class B(A):
    pass


class C(A):
    pass


B.x = 2
A.x = 3
print A.x, B.x, C.x