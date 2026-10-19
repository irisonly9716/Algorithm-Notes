class Solution:
    # approach2: backtracking; we can use DP as well.
    def partition(self, s: str) -> list[list[str]]:
        
        if not s:
            return []

        res = []
        path = []
        n = len(s)

        def backtracking(start) -> None:

            if start == n:
                res.append(path.copy())
                return

            for i in range(start, n):
                sub_s = s[start:i + 1]
                if self.is_palindrome(sub_s):
                    path.append(sub_s)
                    backtracking(i + 1)
                    path.pop()

        backtracking(0)
        return res


    # helper; can be optimized. parameters can be indexes. 
    def is_palindrome(self, sub_s) -> bool:

        if not sub_s:
            return True

        n = len(sub_s)
        left = 0
        right = n - 1

        while left < right:

            if sub_s[left] != sub_s[right]:
                return False

            left += 1
            right -= 1

        return True


# 时间：O(n² · 2^n)，最多 O(2^n) 个节点，每个节点 O(n) 次切片 + O(n) 回文判断
# 空间：O(n)，递归深度与 path 长度（不计结果数组）
# 如果不切片直接indexes在原数组上判断是否回文 可以优化时间到O(n · 2^n)