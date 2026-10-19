
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not target or not candidates:
            return []

        candidates.sort() # O(n log n) for trimming
        path = []
        res = []
        n = len(candidates)

        def backtracking(remain, start) -> None:

            if remain == 0:
                res.append(path[:])
                return 

            # if remain < 0, we don't need to go to the next layer of recursion because there
            # is no way the sum(path) == target
            # but if we sort the candidates, we don't even need to do this
            # if remain < 0:
                # return 

            for i in range(start, n):

                # Trim, break the for loop
                if remain - candidates[i] < 0:
                    break

                path.append(candidates[i])
                backtracking(remain - candidates[i], i) # this candidates[i] can be used again
                path.pop()

        backtracking(target, 0)
        return res
    
# T 为target，m 为 candidates 中最小的数
# O(n^(T/m + 1)) 级别（宽松上界），排序 O(n log n) 被完全淹没 -> 最多要选 T/m 个数，最坏情况每个数都可以选 n 个数，递归树的深度为 T/m
# 空间：O(T/m)，递归栈与 path 的最大深度，不计结果数组
