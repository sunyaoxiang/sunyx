# -*- coding: utf-8 -*-

# from threading import Thread
# import time
#
# def _sum(x, y):
#     print("Compute {} + {}...".format(x, y))
#     time.sleep(2.0)
#     return x+y
# def compute_sum(x, y):
#     result = _sum(x, y)
#     print("{} + {} = {}".format(x, y, result))
#
# start = time.time()
# threads = [
#     Thread(target=compute_sum, args=(0,0)),
#     Thread(target=compute_sum, args=(1,1)),
#     Thread(target=compute_sum, args=(2,2)),
# ]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("Total elapsed time {} s".format(time.time() - start))
#
# # Do not use Thread
# start = time.time()
# compute_sum(0,0)
# compute_sum(1,1)
# compute_sum(2,2)
# print("Total elapsed time {} s".format(time.time() - start))


from threading import Thread
import time


# class ComputeSum(Thread):
#     def __init__(self, x, y):
#         super(ComputeSum,self).__init__()
#         # Thread.__init__(self)
#         self.x = x
#         self.y = y
#     def run(self):
#         result = self._sum(self.x, self.y)
#         print("{} + {} = {}".format(self.x, self.y, result))
#     def _sum(self, x, y):
#         print("Compute {} + {}...".format(x, y))
#         time.sleep(2.0)
#         return x+y
#
# threads = [ComputeSum(0,0), ComputeSum(1,1), ComputeSum(2,2)]
# start = time.time()
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("Total elapsed time {} s".format(time.time() - start))


# from threading import Thread, Lock
# import time
# _base = 1
# _lock = Lock()
# class ComputeSum(Thread):
#     def __init__(self, x, y):
#         super(ComputeSum,self).__init__()
#         self.x = x
#         self.y = y
#     def run(self):
#         result = self._sum(self.x, self.y)
#         print("{} + {} + base = {}".format(self.x, self.y, result))
#     def _sum(self, x, y):
#         print("Compute {} + {}...".format(x, y))
#         time.sleep(2.0)
#         global _base
#         with _lock:
#             result = x + y + _base
#             _base = result
#         return result
# threads = [ComputeSum(0,0), ComputeSum(1,1), ComputeSum(2,2)]
#
# start = time.time()
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("Total elapsed time {} s".format(time.time() - start))
#
# _lock.acquire()
# try:
#     result = x + y + _base
#     _base  = result
# finally:
#     _lock.release()


from threading import Lock,Thread
_base_lock = Lock()
_pos_lock  = Lock()
_base = 1

def _sum(x, y):
    # Time 1
    with _base_lock:
        # Time 3
        with _pos_lock:
            result = x + y
    return result
def _minus(x, y):
    # Time 0
    with _pos_lock:
        # Time 2
        with _base_lock:
            result = x - y
    return result

print _sum(1,2)
print _minus(3,4)
print _sum(5,6)


