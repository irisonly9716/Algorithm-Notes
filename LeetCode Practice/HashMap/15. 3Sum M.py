from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # approach:sort + two pointers. 
        # mind the possible duplicate results: each position of triplets can't be same value.

        n = len(nums)
        if n < 3:
            return []

        nums.sort()
        res = []

        # tripets, make sure we will have 3 elements to sum up.
        for i in range(n-2):

            # ⭐trim
            if nums[i] > 0:
                break

            # the first place of triplets can't be same as the previous valid one.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                num = nums[i] + nums[left] + nums[right]

                if num > 0:
                    right -= 1
                
                elif num < 0:
                    left += 1

                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # ⭐make sure 1. the second element and third element won't repeat. 2.the indexes won't exceed.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

# TC:O(n log n + n ** 2) 
# SC:O(1) if the output doesn't matter.
# why n ** 2 even though the [left, right] will become smaller since i++?
# 'Cuz n → n-1 → n-2 → n-3 → ... is a linear way to become smaller; if n → n/2 → n/4 → ... then it should be log n

