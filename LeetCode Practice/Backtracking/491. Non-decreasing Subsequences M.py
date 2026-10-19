from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        # approach: backrtracking + set for removing duplicates in the same layer(same position)
        # we cannot sort the nums because subsequence should in original order        
        # subsequence是不可以改变顺序的
        # 长度大于等于2即可加入res数组
        # 需要去重？ 同个位置不可以选择同个数 即for循环中不可以同个数 即同层递归不能使用相等的数字
        # 还是组合问题 不是排列 

        res = []
        

        def backtracking(path, index) -> None:

            if len(path) >= 2:
                res.append(path.copy())  # 这里不return因为还有更多的长度要计入 就等for循环自动结束即可

            # 每一层去重是在for循环上方这个位置设置新的visited数组
            visited = set()

            for i in range(index, len(nums)):

                # 不能排序所以只能visited数组去重
                if nums[i] in visited:
                    continue

                # 只有当前升序 这个位置才会选择这个数字 否则无效 继续选择这个位置的下一个可能性（for循环继续）
                # 同时需要考虑如果当前没有path  也需要加入一个数
                if not path or (path and nums[i] >= path[-1]):

                    path.append(nums[i])
                    visited.add(nums[i]) # 这里是只add不必remove 因为同层的visited没有要去掉数的逻辑

                    backtracking(path, i + 1)

                    path.pop()

        backtracking([], 0)

        return res

    # time: O(2^n) 每个数字都有选和不选的可能性
    # space: O(n) 递归深度最深是n个数字组成的子集
    # 启示：
    # 如果是同层去重不能排序的情况下就只能在for循环前面写visited就是在同一个for循环下（同个position）不能重复 ；
    # 如果是同branch不可重复 那就在for循环里面写 跨越递归层级 纵向不重复（全排列II）
