from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        # approach: backtracking + sort for removing duplicate elements in same position to aviod same permutations 
        # + set for removing duplicate indexes in same branch

        if not nums:
            return []

        path = []
        res = []
        n = len(nums)
        nums.sort()
        visited = set() # store indexes

        def dfs() -> None:

            if len(path) == n:
                res.append(path.copy())
                return

            for i in range(n):
                
                # if nums[i] == nums[i - 1] and the previous (i-1) index is used: continue
                # i - 1 in 或 not in visited 都是成立的 是树层去重和树枝去重的差别
                if i > 0 and nums[i] == nums[i - 1] and i - 1 in visited:
                    continue
                if i in visited:
                    continue

                path.append(nums[i])
                visited.add(i)
                dfs()
                path.pop()
                visited.remove(i)

        dfs()
        return res

# time: O(n!) 每个数字都有n次选择 所以是n*n-1*n-2*...*1 = n! ⭐P(n,n) = n!
# space: O(n) 递归深度最深是n个数字组成的排列