# coding=utf-8
import multiprocessing
import time


def prf(i=None):
    print i
    time.sleep(0.5)

def main_i():
    print 'main'
    list = ['xa','sd','gw','dw','we','dfad','weq','rqwd','xa','sd','gw','dw','we','dfad','weq','rqwd','xa','sd','gw','dw','we','dfad','weq','rqwd']
    pool = multiprocessing.Pool(processes=10)
    for i in range(0,len(list)):
        pool.apply_async(prf,args= (list[i],))
    pool.close()
    pool.join()

    print 'main over'

if __name__ == '__main__':
    main_i()