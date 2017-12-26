# -*- coding: utf-8 -*-

def inc():
    x = [0]

    def inner():
        x[0] += 1
        print x[0]

    return inner


inc1 = inc()
inc2 = inc()

a = inc1.__closure__[0].cell_contents
b = inc1.__name__
inc1()
inc1()
inc1()
inc2()
pass