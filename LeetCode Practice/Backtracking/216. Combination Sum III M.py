from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        if k == 0 or n == 0:
            return []

        res = []
        path = []

        def backtracking(curr_sum, start) -> None:

            if len(path) == k and curr_sum == n:
                res.append(path[:])
                return

            if len(path) >= k or curr_sum > n:
                return 

            for num in range(start, 10):

                path.append(num)
                backtracking(curr_sum + num, num + 1) # ⭐ this must be num + 1 not start + 1
                path.pop()

        backtracking(0, 1)
        return res

            

            
# C(9, k) 同时 和为n
# O(1) deepest = 9



