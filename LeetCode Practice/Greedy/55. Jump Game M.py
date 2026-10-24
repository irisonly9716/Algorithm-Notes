from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # approach:dp/greedy
        # we use further step each time we reach an index
        step = 0

        for i in range(len(nums)):
            
            if i > step:
                return False
            step = max(i + nums[i], step)
            
        return True
            