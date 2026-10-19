from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # approach: recursion + sort for removing duplicates in the same position

        # 求全集 但是是数组里面有重复的数字可以选 但同个位置不可以选相等的数否则会有重复集合
        # 所以是index去重+for循环相等数字去重

        # 为什么不用used数组？ 因为首先有空间开销 其次全局used数组更适合避免相同数字在不同位置互换生成重复排列 也就是在全排列中使用
        # 在递归中用used 来避免同branch没有重复数字也不可以 因为只要不是同index 数字的值可以重复

        # 去重需要排序 要把相同值集中在一起才能进行层级去重
        res = []
        nums.sort()

        def backtracking(path, start) -> None:

            res.append(path.copy())
            

            for i in range(start, len(nums)):

                # 同个位置不可以选相等的数 否则重复集合
                # 但是首先递归下去的第一个数是可以的 因为是不同位置
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])

                backtracking(path, i + 1)

                path.pop()

        backtracking([], 0)

        return res