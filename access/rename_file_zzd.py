# coding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import os
import ConfigParser;
import pymssql, json, io, logging, time, datetime, signal, multiprocessing, functools, threading, xlwt, xlrd


def scan_files(directory, prefix=None, postfix=None):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list

# for file_name in file_names:
# # print file_name
# # print file_name[0],file_name[1]
#     try:
#         os.rename(file_name[0],file_name[1])
#     except:
#         file_name

# Dir_name = "./"
# file_names = scan_files(Dir_name,postfix ='.xlsx')
# for file_name in file_names:
#     new_file_name = str(file_name.replace(' ','')).replace('..xlsx','.xlsx')
#     print file_name,'\n',new_file_name,'\n'
#     os.rename(file_name,new_file_name)



Dir_name = "./"
file_names = scan_files(Dir_name, postfix='.xls')
for file_name in file_names:
    # # 000698.SZ_200S-07-28_12.42.xlsx
    # ticker_id = file_name[2:8].replace('X','S')
    # exchange_cd = file_name[8:12]
    # publish_date = file_name[12:22].replace('X','S')
    # file_name_end = str(file_name[22:].replace('X','S'))
    # new_file_name = './'+ticker_id+exchange_cd+publish_date+file_name_end
    new_file_name = file_name.replace('收益率曲线明细数据', '中债指数样本券数据(历史)')
    # new_file_name = new_file_name.replace(',','')
    print file_name, new_file_name
    if file_name != new_file_name:
        print file_name, new_file_name
        os.rename(file_name, new_file_name)