# -*- coding: utf-8 -*-

# s = 'coffee'
#
# print s.rindex('f')


# s = 'helooohel'
#
# print s.rstrip("hel")


# print("{}\n{}\n{}\n{}\n{}".format(
#     "hello, WORLD".upper(),
#     "hello, WORLD".lower(),
#     "hello, WORLD".swapcase(),
#     "hello, WORLD".capitalize(),
#     "hello, WORLD".title()))

# print("""
# {}|{}
# {}|{}
# {}|{}
# {}|{}
# {}|{}
# {}|{}
# {}|{}
# """.format(
#     "Python".startswith("Py"),"Python".startswith("y"),
#     "Python".endswith("on"),"Python".endswith("o"),
#     "i23o6".isalnum(),"1 2306".isalnum(),
#     "isalpha".isalpha(),"isa2pha".isalpha(),
#     "12345".isdigit(),"isdigit".isdigit(),
#     "python".islower(),"Python".islower(),
#     "PYTHON".isupper(),"Python".isupper(),
# ))

# li = ['test ', 'format' , ' good']
# print "i think {} {} is {} ".format(*li)

# li = ['test ', 'format' , ' good']
# print "i think {0[0]} {1} is {0[2]} ".format(li,"cache")


li = {'test':'test ', 'format':'format' ,'good':'good'}
print "i think {test} {good} is {good} ".format(**li)
print "i think {0[test]} {0[good]} is {0[good]} ".format(li)
#
# print '{string:->50}'.format(string ='string')
# print '{0:-<50}'.format('string')
# print '{0:-^50}'.format('string')
#
# print '{:0=50}'.format(100)

# print '{0:>7}'.format('string')

# print "{0}\n{1}\n{0}".format(3.14, -3.14)
# print "{0}\n{1}\n{0}".format(3.14, -3.14)
# print "{0:+}\n{1:-}\n{0: }".format(3.14, -3.14)

# print "{0:b} {0:#b}".format(3)
# print "{0:a=16}".format(3)

# print "{0:.6}\n{0:.100}".format(6.0111111112312)

# print(b"Python")
# python = (b'P' b'y' b"t" b'o' b'n')
# print(python)

# print b"Python"[0]
#
# print(b'\xff'[0])
# print(b'\x24')

# print("$".encode('ascii'))
# print("$".encode('ascii')[0])