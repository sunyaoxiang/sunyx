# coding=utf-8
import os

#print os.listdir('D:\\')
#print os.listdir(os.getcwd())

#os.mkdir('temp')
#os.rmdir('temp')

#print os.getenv('path')
#print os.path.split('D:\Python\data_ibor.git')

# a = 'D:\Python\data_ibor.git\README.md'
# b = 'D:\Python'
#
# os.curdir
# print os.path.split(a),os.path.split(b)
# print os.path.isfile(a),os.path.isfile(b)
# print os.path.isdir(a),os.path.isdir(b)

# a = 'D:\Python\data_ibor.git'
# b = 'D:\Python'
# print os.listdir('.')
# os.chdir(a)
# print os.listdir('.')
# os.curdir
# print os.listdir('.')

a = u'D:\Work\macro_data excel自动更新'
l = os.listdir(a)
for i in l:
    print i
b = 'D:\Python'
# print os.path.normpath(a)

# for i in os.listdir('.'):
#     if os.path.isfile(i) == True:
#         print os.path.abspath(i),'%sb'%os.path.getsize(i)

# for i in os.listdir('.'):
#     if os.path.isfile(i) == True:
#         print os.path.splitext(i),'%sb'%os.path.getsize(i)
# print os.path.basename(b)
# print os.path.dirname(b)