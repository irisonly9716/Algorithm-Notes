from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
 
        # Approach: same as 3Sum but we need double loops now. two pointers + sort, mind duplicate results.

        n = len(nums)
        if n < 4:
            return []

        nums.sort()
        res = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    num = nums[i] + nums[j] + nums[left] + nums[right]

                    if num > target:
                        right -= 1
                    
                    elif num < target:
                        left += 1

                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # ⭐make sure 1. the second element and third element won't repeat. 2.the indexes won't exceed.
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        
        return res

# TC:O(n log n + n ** 3)
# SC:O(1) excluding the output




