from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # approach: backtracking
        if not s:
            return []

        path = []
        res = []
        n = len(s)

        def backtracking(start) -> None:

            if len(path) == 4:
                if start == n:
                    res.append('.'.join(path))
                return

            # i can't exceed n; s[start:i] 
            # i not included, so i can equal to n
            for i in range(start + 1, min(start + 4, n + 1)):

                sub_s = s[start:i] # i not included
                if len(sub_s) >= 2 and s[start] == '0':
                    break

                num = int(sub_s)
                if 0 <= num <= 255:
                    path.append(sub_s)
                    backtracking(i)
                    path.pop() 

        backtracking(0)
        return res      


# O(1)
# O(1)
# IP 固定 4 段、每段最多 3 种长度，搜索树最多 3^4 = 81 个叶子，所以时间和空间都是 O(1)



