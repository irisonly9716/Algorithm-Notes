from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # approach: greey - Kadane Algorithm
        # when we find a num that will make the target <= 0, restart the curr subarray
        # because a negative/0 number will never make a sum bigger

        curr_sum = 0
        best = max(nums) # record the max first

        for num in nums:

            if num + curr_sum > 0:
                curr_sum += num
                best = max(curr_sum, best) # must record best in here

            else:
                curr_sum = 0

            # never record best in here, it may become 0 even though 0 is not in array.

        return best
