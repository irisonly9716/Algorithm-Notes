from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # approach:greedy
        # rule: we try to reach each station(index), +gas-cost, once tank < 0, station can't be reached
        # brute force: try starting from each station and see if success n^2

        # edge case: 
        if sum(gas) < sum(cost):
            return -1

        start = 0
        curr = 0

        for i in range(len(gas)):

            curr += gas[i] - cost[i]
            
            # if curr gas < 0, the curr start can't be valid, try the next one
            if curr < 0:
                curr = 0
                start = i + 1

        return start

# 推导1：从 s 出发在 i 卡住，那么 s 到 i 之间的任何站出发也一定在 i 卡住, 这条结论保证了 start = i + 1 可以直接跳过一大段，不用一个个重试。
# 推导2：如果总油量大于总消耗量，那么一定存在一个起点可以绕一圈。
        

        
        '''
        # brute force n^2

        if sum(cost) > sum(gas):
            return -1


        # for 循环以每个index的加油站为起点尝试
        for start in range(len(gas)):

            # 每个起点都有初始油箱
            tank = 0
            can_complete = True

            # 内层循环模拟从start开始绕一圈的情况
            for i in range(len(cost)):

                # 计算一圈的index
                index = (start + i) % len(gas)
                tank += gas[index]
                tank -= cost[index]

                # 如果tank在某一点小于0，设为false
                if tank < 0:
                    can_complete = False
                    break

            # 如果有一层循环的情况 是 可以完成（中途没有设为false并退出
            # 说明这个start可以成立
            if can_complete:
                return start

        return -1

        '''