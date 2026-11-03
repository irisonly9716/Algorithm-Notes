from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # approach1（most efficient）: two pointers 
        # vertically calculate the water trapped in each col.
        # ⭐buckets effect: for each curr col, if left highest is lower than right highest,
        # the lower side should be calculated, water += lower_highest - height of curr col.
        
        n = len(height)
        left_highest = 0
        right_highest = 0
        left = 0
        right = n - 1
        water = 0

        # when left == right, they are unable to trap water
        while left < right:

            left_highest = max(left_highest, height[left])
            right_highest = max(right_highest, height[right])

            if left_highest < right_highest:
                water += left_highest - height[left]
                left += 1

            else:
                water += right_highest - height[right]
                right -= 1

        return water


# TC:O(n) each element is visited at most once
# SC:O(1) only 4 pointers and 2 highest values are used

# approach2: monotonic stack
# horizontally calculate the water. 
# water += (distance between the curr col and the left highest col * height of the left highest col and the right highest col)
# monotonic stack: stack(index) DESC, when the curr height is higher than stack[-1], we can pop the stack and calculate the water trapped by the popped coL and the current col. 
# horizontally calculate the water trapped in each col, the water trapped by the popped col is determined by the distance between the curr col and the left highest col, and the height of the left highest col and the right highest col.