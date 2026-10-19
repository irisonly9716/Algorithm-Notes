class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        if not candidates or not target:
            return []

        path = []
        res = []
        candidates.sort() # for removing duplicates
        n = len(candidates)

        def backtracking(remain, start) -> None:

            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, n):

                # trim
                if remain - candidates[i] < 0:
                    break

                # remove duplicates in the same position
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                # each elements can be used only once
                backtracking(remain - candidates[i], i + 1)
                path.pop()

        backtracking(target, 0)
        return res

# T 为target，m 为 candidates 中最小的数
# O(n^(T/m + 1)) 级别（宽松上界）+ O(n log n) 排序被完全淹没 -> 最多要选 T/m 个数
# 空间：O(T/m)，递归栈与 path 的最大深度，不计结果数组