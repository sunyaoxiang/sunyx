# coding=utf-8
import multiprocessing
import time


def prf(i=0,j=0):
    for t in range(i,j):
        print t
        time.sleep(0.05)

def main_i():
    print 'main'
    prf(50,55)
    pl =[]
    multiprocessing.freeze_support()
    pl.append(multiprocessing.Process(target= prf,args=(1,10)))
    pl.append(multiprocessing.Process(target= prf,args=(10,20)))
    pl.append(multiprocessing.Process(target= prf,args=(20,30)))
    for p in pl:
        p.start()
    p.join()

    print 'main over'

if __name__ == '__main__':
    main_i()