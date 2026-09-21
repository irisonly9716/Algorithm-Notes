from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # approach:sliding window
        # 1. use 2 pointers to iterate the array, both from the start 
        # 2. when sum >= target, compare the length of window to the min_win
        # 3. return min_win

        # maintain the variable of minumum window, keeping it the min length. If window not found, return 0.
        min_win = float('inf')

        n = len(nums)
        left = 0

        # the sum of the current window
        curr_sum = 0 

        for right in range(n):

            num = nums[right]
            curr_sum += num

            # while we found a valid window, record and try to move the left pointer to shrink the window from left
            while curr_sum >= target:

                # mind the way to compute length in an array. the left boarder should be included.
                length = right - left + 1  
                min_win = min(length, min_win)
            
                curr_sum -= nums[left]
                left += 1


        return min_win if min_win != float('inf') else 0

# test
s= Solution()
target = 7
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))

# TC:O(n)
# SC:constant