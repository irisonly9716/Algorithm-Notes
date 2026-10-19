class Solution(object):
    def subsets(self, nums):

        # approach: recursion, collect all possible conbinations on each leave in a search tree.
        res = []
        path = []
        n = len(nums)

        def backtracking(start):

            res.append(path[:]) # record first and then return

            if start == n: # we don't need to return actually, the for loop will stop.
                return

            for i in range(start, n):

                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return res


# time: O(2^n) 子集问题是选和不选的问题 每个数字都有n次选和不选
# space O(n) 递归深度最深是n个数字组成的子集

