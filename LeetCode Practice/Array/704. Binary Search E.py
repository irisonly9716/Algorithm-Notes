from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # approach:plain binary search
        # mind the boarders of array
        
        n = len(nums)

        i = 0
        j = n - 1

        while i <= j:

            mid = i + (j - i) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                j = mid - 1

            else:
                i = mid + 1

        return -1

# test
s= Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(s.search(nums, target))
 
# TC:log n
# SC:constant