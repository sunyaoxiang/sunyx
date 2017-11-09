# -*- coding: utf-8 -*-


# sq = reduce(lambda x,y : x+y , range(6,10))
# print sq  # 30



# sq = map(lambda x:x+10 , range(1,6))
# print sq # [11, 12, 13, 14, 15]

# sq = [ x for x in range(10)]
# print sq # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# sq = filter(lambda x : x % 2 == 0 , range(10))
# print sq # [0, 2, 4, 6, 8]


sq = [x for x in range(10) if x %2 == 0]
print sq # [0, 2, 4, 6, 8]