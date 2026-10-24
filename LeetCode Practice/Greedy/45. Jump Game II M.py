from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # approach:greedy
        # we only count 1 jump if we reach the curr further
        # and update the further

        if len(nums) <= 1:
            return 0

        jump = 0
        further = 0 # next farest index we can reach
        end = 0 # current farest index we can reach

        for index in range(len(nums) - 1): # the last index doesn't need any jump

            further = max(index + nums[index], further) # update the next farest index we can reach

            if index == end:
                jump += 1
                end = further # update the current farest index we can reach
            

        return jump

