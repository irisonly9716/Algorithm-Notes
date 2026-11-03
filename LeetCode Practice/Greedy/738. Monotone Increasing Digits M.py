class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        # approach:greedy
        # iterate the digits in reverse order, if the right one is smaller than or equal left one, modify the right "9", the left - 1
        # if we have the result "09", make it "9", no leading "0"

        path = list(str(n))
        m = len(path)
        flag = m  # 从 flag 开始往后都填 9，默认不填

        # 从后往前遍历
        for i in range(m - 2, -1, -1):
            if path[i] > path[i + 1]:          # 严格大于才需要处理
                path[i] = str(int(path[i]) - 1)
                flag = i + 1                   # 更新填 9 的起点 所有当前-1的digit之后的digits都要改为9

        # flag 及之后全部变 9
        for i in range(flag, m):
            path[i] = '9'

        return int(''.join(path)) # 返回结果，变成int会自动去掉前导 0

# TC:O(d) d is the number of digits of n, so O(log n)
# SC:O(d) the list of digits
