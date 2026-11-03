from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        # approach: monotonic stack(index), ASC
        # when we encounter a higher height in the heights, pop the stack[-1](while loop)
        # and calculate the area = height[stack[-1]] * (index - stack[-1] + 1)

        heights = [0] + heights + [0] # ⭐ Make sure all cols will be popped from stack and calculated
        stack = [] # index, ASC
        max_area = 0

        for index in range(len(heights)):
            while stack and heights[stack[-1]] > heights[index]:
                height = heights[stack.pop()]
                # 因为stack里面是单调递增的 所以当前pop掉的col的右边（这个while循环pop出去过的col）都比col大
                # 所以distance是[col, 右边极限的col 也就是当前index前面一个] = (stack[-1],index) 
                # 所以用index - stack[-1] - 1来算距离
                distance = index - stack[-1] - 1 # ⭐ when the col is popped, the distance is the (stack[-1],index)  
                area = distance * height
                max_area = max(area, max_area)

            stack.append(index)

        return max_area

# TC:O(n) each element is pushed and popped at most once
# SC:O(n) stack