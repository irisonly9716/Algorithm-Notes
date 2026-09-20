'''
彩票中奖功能

输入nums 里面是id, weight的tuple
表示这个id有多少赢的权重
返回k个winner


'''


import random, heapq
from typing import List, Tuple

class Solution:
    def findTopKWinner(self, nums: List[Tuple[int, int]], k: int) -> List:

        n = len(nums)

        if k > n:
            return [_id for _id, weight in nums]
        if k == 0:
            return []
        

        heap = []

        for _id, weight in nums:
            
            # for every id, calculate a value with a random seed.
            rand = random.random()
            val = rand ** (1 / weight) # if weight is bigger, val will be bigger

            heapq.heappush(heap, (val, _id)) # use min_heap to store values

            if len(heap) > k:
                heapq.heappop(heap) # pop smallest value

        return [_id for _, _id in heap]


# n log k; k
# 经典的彩票抽奖 按权重抽多个人 且 不放回去pool
# 如果只抽一次 可以log n 就是528.Random pick with weight (prefix + binary search)




        '''
        # k怎么处理？ 可以是k %= n 或者 如果k > n, 返回所有id
        heap = []
        
        for _id, weight in nums:

            # 每个候选人要有一个随机数 否则的话 还是按照weight在排序 并不是随机的top k！！
            rand_int = random.random() # 随机数 返回的是一个[0,1)区间的float 不包含1
            random_val = rand_int ** (1 / weight) # rand_int小于1 
            heapq.heappush(heap, (random_val, _id)) # weight越大，val越大 所以需要min_heap, 小的被淘汰
            
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _, _id in heap:
            res.append(_id)

        return res
        '''
