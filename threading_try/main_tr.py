# coding=utf-8
from juti import ptf
import threading





threads = []
t1 = threading.Thread(target= ptf,args=(0,5))
t2 = threading.Thread(target= ptf,args=(5,10))
threads.append(t1)
threads.append(t2)

for t in threads:
    t.setDaemon(True)
    t.start()
t.join()