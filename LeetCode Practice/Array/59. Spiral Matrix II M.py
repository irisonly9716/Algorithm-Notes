from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # approach: simulations
        # 1. construct the empty matrix, maintain the 4 boarders of the matrix
        # 2. for loop maintains the 4 boarders and record the elements.

        
        left = up = 0
        right = bottom = n - 1
        matrix = [[0] * n for _ in range(n)]
        num = 1

        while left <= right or up <= bottom:

            # record from left to right at the current top, the raw is not changing but column is changing.
            for j in range(left, right + 1):
                matrix[up][j] = num
                num += 1
            up += 1

            for i in range(up, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # record from right to left at the current bottom
            # Compare to 54, this is a matrix so that we don't need to worry about we don't actually have the rest part that is not visited 
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1

      
            for i in range(bottom, up - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix

# test
s = Solution()
n = 3
print(s.generateMatrix(n))

# TC:O(n**2）
# SC:O(n**2) if the output matters, otherwise O(1).