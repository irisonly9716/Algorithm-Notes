from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # we can compute all elements and then sort the new array but it's not efficient. (n log n)
        # approach:3 pointers. 1 from the start, 1 from the end, 1 for putting the position in the new array 

        n = len(nums)
        ans = [0] * n

        i = 0
        j = k = n - 1 # k is the pointer to put new elements in the new array 
        
        while k >= 0:

            if nums[i] ** 2 >= nums[j] ** 2:
                ans[k] = nums[i] ** 2
                i += 1

            else:
                ans[k] = nums[j] ** 2
                j -= 1

            k -= 1

        return ans

# test
s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))

# TC:n
# SC:n (the output array. If it does not count, the space complexity would be constant.)
        
