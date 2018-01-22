# -*- coding: utf-8 -*-
def print_directory_contents(sPath):
    import os

    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print sChildPath


# dir = "D:\\Python"
# print_directory_contents(dir)
#
# import os
# # os.chdir(dir)
# # os.listdir(dir)
# # os.listdir(dir)
# print os.path.abspath(os.listdir(dir)[0])
# a = os.path.dirname(os.listdir(dir)[0])
# print os.path.dirname(os.path.abspath(dir))
# print os.path.dirname(os.path.dirname(os.path.abspath(dir+"\02_to_03")))
# pass

#
# def f(x,l=[]):
# for i in range(x):
# l.append(i*i)
#     print l
#
# f(2)
# f(3,[3,2,1])
# f(3)

#
# def f2(arg1,arg2,*args,**kwargs):
#     print arg1,arg2, args, kwargs
# l = [1,2,3]
# t = (4,5,6)
# d = {'a':7,'b':8,'c':9}
# f2(1,2,4,5,6,*t,q="winning",**d)


class A(object):
    def go(self):
        print "go A go!"

    def stop(self):
        print "stop A stop!"

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print "go B go!"


class C(A):
    def go(self):
        super(C, self).go()
        print "go C go!"

    def stop(self):
        super(C, self).stop()
        print "stop C stop!"


class D(B, C):
    def go(self):
        super(D, self).go()
        print "go D go!"

    def stop(self):
        super(D, self).stop()
        print "stop D stop!"

    def pause(self):
        print "wait D wait!"


class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()

# 说明下列代码的输出结果
print D.mro()
# a.go()
# b.go()
# c.go()
# d.go()
# e.go()
#
# a.stop()
# b.stop()
# c.stop()
# d.stop()
# e.stop()
#
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()