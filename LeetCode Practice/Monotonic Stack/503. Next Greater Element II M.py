from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # approach: monotonic stack
        # iterate twice of the nums, until completing the iteration 

        n = len(nums)
        res = [-1] * n
        stack = [] # monotonic, DESC, index

        for i in range(n * 2):
            index = i % n
            while stack and nums[stack[-1]] < nums[index]:
                curr_index = stack.pop()
                res[curr_index] = nums[index]

            # ⭐: only when i < n (the first round of iteration, we add the index to stack)
            if i < n:
                stack.append(index)

        return res

# TC:O(n) 2n iterations, every index is pushed and popped at most once
# SC:O(n) the stack
