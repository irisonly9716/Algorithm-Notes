from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        # approach:greedy
        # make bigger positive numbers
        # sort the nums by absolute values desc
        # try to make each negative num positive (k-1) 

        nums.sort(key=lambda n:abs(n), reverse=True)

        for i in range(len(nums)):

            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
                if k == 0:
                    break

        # if all num is positive and k still > 0, if k is odd, make the smallest positive num negative
        if k > 0 and k % 2 != 0:
            nums[-1] = - nums[-1]

        return sum(nums)
