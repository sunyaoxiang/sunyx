# -*- coding: utf-8 -*-


from heapq import *

# heap = []
# for i in range(3,0,-1):
# heappush(
# heap,i
#     )
# # heappush(heap,3)
# # heappush(heap,2)
# # heappush(heap,1)
# print heap


# heap = list(reversed(range(5)))
# print("List: ", heap)
# heapify(heap)
# print("Heap: ", heap)


# heap = [5,4,3,2,1]
# heapify(heap)
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))

# from queue import PriorityQueue as PQueue
# pq = PQueue()
# pq.put((5,'Python'))
# pq.put((4,'C'))
# pq.put((3,'Js'))
#
# while not pq.empty():
#     a = pq.get()
#     print a[1]

# lstA = [1,2,3,4,5]
# lstB = [1,2,3,4,5]
#
# poped = heapreplace(lstA, 0)
# print("lstA: ", lstA, "poped: ", poped)
#
# # is equal to...
# poped = heappop(lstB)
# heappush(lstB, 0)
# print("lstB: ", lstA, "poped: ", poped)
#
# print("*"*40)
#
# poped = heappushpop(lstA, 9)
# print("lstA: ", lstA, "poped: ", poped)
#
# # is equal to...
# heappush(lstB, 9)
# poped = heappop(lstB)
# print("lstB: ", lstB, "poped: ", poped)

# item = 0
# lstA = [1,2,3,4,5]
# if item < lstA[0]:
#     # replace
#     poped = lstA[0]
#     lstA[0] = item
#     print("lstA: ", lstA, "poped: ", poped)