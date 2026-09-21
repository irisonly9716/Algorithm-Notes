from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # remove elements those are equal to val in place. return: how many elements left.
        # appraoch:two pointers.
        # 1. for loop itterate the array. 2. when nums[i] != val, put nums[i] in k's place. k++;

        n = len(nums)
        # k is a pointer as well as a counter
        k = 0 

        for i in range(n):

            # when nums[i] != val, put nums[i] in k's place. k++;
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# test
nums = [3,2,2,3]
val = 3
s = Solution()
print(s.removeElement(nums, val))

# TC:n
# SC:constant