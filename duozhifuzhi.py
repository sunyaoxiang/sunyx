# -*- coding: utf-8 -*-

msg = "hello"
a,_,_,_,e = msg
print a,e


a,*_,e = msg
print a,e