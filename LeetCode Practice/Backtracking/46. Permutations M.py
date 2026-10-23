from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []

        path = []
        res = []
        n = len(nums)
        visited = set() # for removing duplicates in the same branch in a search tree.

        def dfs() -> None:

            if len(path) == n: # collect the path when we get enough elements
                res.append(path.copy())
                return

            for i in range(n):

                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    dfs()
                    path.pop()
                    visited.remove(nums[i])

        dfs()
        return res



# time: O(n!) 每个数字都有n次选择 所以是n*n-1*n-2*...*1 = n! ⭐P(n,n) = n!
# space: O(n) 递归深度最深是n个数字组成的排列