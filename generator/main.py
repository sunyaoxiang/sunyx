# -*- coding: utf-8 -*-

def my_gen():
    n = 1
    print('This is printed first, n= ', n)
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second, n= ', n)
    yield n

    n += 1
    print('This is printed at last, n= ', n)
    yield n

    n = 10
    print('This is printed at last, n= ', n)
    yield n


for item in my_gen():
    print(item)